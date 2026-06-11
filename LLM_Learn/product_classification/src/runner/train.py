"""
    训练脚本
"""

import time
from dataclasses import dataclass

import torch
import torch.optim as optim
from torch.utils.data import DataLoader
# 日志保存用
from torch.utils.tensorboard import SummaryWriter
# 加载进度条消息
from tqdm import tqdm
from transformers import AutoTokenizer,AutoModelForSequenceClassification,DataCollatorWithPadding

from sklearn.metrics import accuracy_score,f1_score

from common.config import *
from process.dataset import get_dataset

# 训练的配置类

@dataclass
class TrainConfig:
    epochs: int = EPOCHS
    batch_size: int = BATCH_SIZE
    learning_rate: float = LEARNING_RATE
    save_steps: int = SAVE_STEPS

    output_dir: str = MODELS_DIR
    log_dir: str = LOGS_DIR

    # 模型保存和早停配置
    early_stop_metric: str = 'loss'
    early_stop_patience: int = 2

# 定义训练器
class Trainer:
    def __init__(self,model,train_dataset,valid_dataset,collate_fn,compute_metrics_fn,device,train_config):
        # 训练参数
        self.train_config = train_config
        # 模型和设备
        self.model = model.to(device)
        self.device = device
        # 优化器
        self.optimizer = optim.Adam(self.model.parameters(),lr=self.train_config.learning_rate)
        # 数据集
        self.train_dataset = train_dataset
        self.valid_dataset = valid_dataset
        # 函数操作
        self.collate_fn = collate_fn
        self.compute_metrics_fn = compute_metrics_fn
        # 日志写入器
        self.writer = SummaryWriter(log_dir=str(Path(self.train_config.log_dir) / time.strftime("%Y_%m_%d-%H_%M_%S")))

        # 全局变量
        self.step = 1
        self.early_stop_best_score = -float('inf') # 判断保存和早停的指标: 最佳分数(初始最小)
        self.early_stop_counter = 0

    # 定义内部函数: 获取数据加载器
    def _get_dataloader(self,dataset):
        dataset.set_format(type='torch')

        # 创建加载器
        dataloader = DataLoader(
            dataset=dataset,
            batch_size=self.train_config.batch_size,
            shuffle=True,
            collate_fn=self.collate_fn,
        )
        return dataloader

    # 内部方法:训练一步迭代
    def _train_one_step(self,inputs):
        self.model.train()

        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        # 1. 前向传播
        outputs = self.model(**inputs)

        # 2. 计算损失
        loss = outputs.loss

        # 3. 反向传播,计算梯度
        loss.backward()

        # 4. 更新参数
        self.optimizer.step()
        self.optimizer.zero_grad()

        return loss.item()

    # 内部方法: 判断是否保存模型和早停
    def _should_stop(self,metrics):
        # 获取真正的早停指标
        metric = metrics[self.train_config.early_stop_metric]
        # 将指标转为得发: 越高越好
        score = -metric if self.train_config.early_stop_metric == 'loss' else metric

        # 如果超过历史最佳得分,就保存模型,继续训练(返回False)
        if score > self.early_stop_best_score:
            self.early_stop_best_score = score
            self.early_stop_counter = 0 # 容忍度计数清零
            tqdm.write("保存模型...")
            self.model.save_pretrained(self.train_config.output_dir)
            return False
        else:
            self.early_stop_counter += 1
            # 如果超过容忍度上限,就早停
            if self.early_stop_counter >= self.train_config.early_stop_patience:
                return True
            else:
                return False
    # 核心方法: 训练
    def train(self):
        # 获取训练集
        train_dataloader = self._get_dataloader(self.train_dataset)
        # 循环迭代多个轮次
        for epoch in range(self.train_config.epochs):
            # 训练
            for inputs in tqdm(train_dataloader,desc=f"Epoch {epoch+1}/{self.train_config.epochs}"):
                # 执行一步迭代,得到损失
                this_loss = self._train_one_step(inputs)

                # 如果迭代够了100次,就记录日志,并判断保存模型
                if self.step % self.train_config.save_steps == 0:
                    # 记录损失
                    self.writer.add_scalar('loss',this_loss,self.step)
                    tqdm.write(f"Epoch:{epoch+1} | Step: {self.step} | Loss: {this_loss:.6f}")

                    # 验证模型
                    metrics = self.evaluate()
                    metrics_str = '|'.join([f'{k}:{v:.6f}' for k,v in metrics.items()])
                    tqdm.write(f"[Evaluate] {metrics_str}")

                    # 判断保存模型是否早停
                    if self._should_stop(metrics):
                        tqdm.write(f"Early Stopped")
                        return
                self.step += 1

    # 核心方法:评估验证,返回一个字段{'loss': 1.34, 'accuracy': 0.92, 'f1': 0.87}
    def evaluate(self)->dict:
        # 获取数据加载器
        dataloader = self._get_dataloader(self.valid_dataset)

        self.model.eval()

        # 验证总损失
        total_loss = 0
        # 定义列表,保存所有数据的预测标签和真实标签
        all_predictions = []
        all_labels = []

        with torch.no_grad():
            for inputs in tqdm(dataloader,desc="Evaluating"):
                inputs = {k: v.to(self.device) for k, v in inputs.items()}
                # 前向传播
                outputs = self.model(**inputs)
                # 累加损失
                total_loss += outputs.loss.item()
                # 统计预测结果并添加到列表
                predictions = torch.argmax(outputs.logits, dim=-1)
                all_predictions.extend(predictions.tolist())
                # 将真实标签添加到列表
                all_labels.extend(inputs['labels'].tolist())
        # 指标1: 平均损失
        loss = total_loss / len(dataloader)
        # 指标2: 其他指标(如accuracy,precision,recall,f1等),返回字典
        metrics = self.compute_metrics_fn(all_predictions,all_labels)
        return {'loss': loss, **metrics}

def train():
    print("训练开始...")

    # 1. 定义设备
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 2. 加载分词器
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_OR_PATH)

    # 3. 加载标签列表,生成双向映射
    with open(MODELS_DIR/LABELS_FILE , 'r', encoding='utf-8') as f:
        labels = f.read().splitlines()
    id2label = {id:label for id, label in enumerate(labels)}
    label2id = {label:id for id, label in enumerate(labels)}

    # 4. 加载模型
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME_OR_PATH,
        num_labels=len(label2id),
        id2label=id2label,
        label2id=label2id,
        )

    # 5. 数据集
    train_dataset = get_dataset(ds_type='train')
    valid_dataset = get_dataset(ds_type='valid')

    # 6.定义函数
    collate_fn = DataCollatorWithPadding(
        tokenizer=tokenizer,
        padding=True,
        return_tensors='pt'
    )

    def compute_metrics_fn(predictions, labels) -> dict:
        accuracy = accuracy_score(labels,predictions)
        f1 = f1_score(labels,predictions,average='weighted')
        return {'accuracy': accuracy,
                'f1': f1,
        }

    # 7. 定义训练器
    train_config = TrainConfig(epochs=EPOCHS,output_dir=MODELS_DIR)
    trainer = Trainer(
        model=model,
        train_dataset=train_dataset,
        valid_dataset=valid_dataset,
        collate_fn=collate_fn,
        compute_metrics_fn=compute_metrics_fn,
        device =device,
        train_config=train_config
    )

    # 8. 训练
    trainer.train()

if __name__ == '__main__':
    train()

