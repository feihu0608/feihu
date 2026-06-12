"""
    评估脚本
"""
import torch
from sklearn.metrics import accuracy_score,f1_score
from transformers import AutoTokenizer,AutoModelForSequenceClassification,DataCollatorWithPadding

from common.config import *
from process.dataset import get_dataset
from runner.train import Trainer, TrainConfig

def evaluate():
    print("评估开始...")

    # 1. 定义设备
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 2. 加载分词器
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_OR_PATH)

    # 3. 加载模型
    model = AutoModelForSequenceClassification.from_pretrained(MODELS_DIR / "best")

    # 4. 数据集
    test_dataset = get_dataset(ds_type='test')

    # 5. 定义函数
    collate_fn = DataCollatorWithPadding(
        tokenizer=tokenizer,
        padding=True,
        return_tensors='pt'
    )

    def compute_metrics_fn(predictions,labels)-> dict:
        accuracy = accuracy_score(labels,predictions)
        f1 = f1_score(labels,predictions,average='weighted')
        return {'accuracy':accuracy,'f1':f1}

    # 6. 定义训练器
    train_config = TrainConfig()
    trainer = Trainer(
        model=model,
        train_dataset=None,
        valid_dataset=test_dataset,
        collate_fn=collate_fn,
        compute_metrics_fn=compute_metrics_fn,
        device=device,
        train_config=train_config,
    )

    # 7. 评估
    metrics = trainer.evaluate()

    print("评估结果",metrics)

if __name__ == '__main__':
    evaluate()




