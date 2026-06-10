'''
    训练脚本，得到最优模型
'''
import time

import torch
from torch import nn, optim
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

from config import *
from dataset import get_dataloader
from transformers import AutoModelForSequenceClassification  # 模型类

# 核心方法：训练一个轮次
def train_one_epoch(model, dataloader, optimizer, device):
    model.train()
    total_loss = 0
    # 按批次进行迭代
    for batch in tqdm(dataloader, desc='训练'):
        # targets = batch.pop('labels').to(device).float()
        inputs = { k:v.to(device) for k,v in batch.items() }

        # 1. 前向传播
        outputs = model(**inputs)

        # 2. 计算损失
        loss = outputs.loss

        # 3. 反向传播，计算梯度
        loss.backward()

        # 4. 更新参数
        optimizer.step()
        optimizer.zero_grad()

        # 累加损失
        total_loss += loss.item()
    return total_loss / len(dataloader)

# 训练主流程
def train():
    # 1. 定义设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # 2. 获取数据加载器
    dataloader = get_dataloader()

    # 3. 定义模型
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME_OR_PATH).to(device)

    # 4. 优化器
    # loss_fn = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    # 引入日志写入器
    writer = SummaryWriter(log_dir=LOGS_DIR / time.strftime('%Y-%m-%d_%H-%M-%S'))

    # 5. 开始训练
    min_loss = float('inf')
    for epoch in range(EPOCHS):
        print("=========", f"Epoch {epoch+1}", "=========")

        # 训练一个轮次，返回平均训练损失
        this_loss = train_one_epoch(model, dataloader, optimizer, device)
        print(f"Loss: {this_loss:.6f}")

        writer.add_scalar('loss', this_loss, epoch+1)

        # 保存模型到文件
        if this_loss < min_loss:
            min_loss = this_loss
            # torch.save(model.state_dict(), MODELS_DIR/BEST_MODEL_FILE)
            model.save_pretrained(MODELS_DIR)
            print("模型保存成功！")
    writer.close()

if __name__ == '__main__':
    train()