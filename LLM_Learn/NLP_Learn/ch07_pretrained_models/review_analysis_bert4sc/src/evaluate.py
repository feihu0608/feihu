'''
    评估脚本
'''

import torch
from tqdm import tqdm

from config import *
from transformers import AutoModelForSequenceClassification
from predict import predict_batch
from dataset import get_dataloader

# 核心逻辑
def evaluate(model, dataloader, device):
    model.eval()
    correct_count = 0
    total_count = 0
    with torch.no_grad():
        # 遍历测试集
        for batch in tqdm(dataloader, desc='评估'):
            targets = batch.pop('labels').tolist()
            inputs = {k: v.to(device) for k, v in batch.items()}

            # 1. 调函数进行预测
            results = predict_batch(model, inputs, device)

            # 2. 对比预测结果和真实标签，统计准确个数
            for result, target in zip(results, targets):
                # 得到预测标签
                label = 1 if result > 0.5 else 0
                if label == target:
                    correct_count += 1
                total_count += 1
    return correct_count / total_count

# 评估主流程
def run_evaluate():
    # 1. 定义设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # 2. 获取数据加载器
    test_dataloader = get_dataloader(train=False)

    # 3. 定义并加载模型
    model = AutoModelForSequenceClassification.from_pretrained(MODELS_DIR).to(device)

    print("模型加载成功！")

    # 调用评估逻辑
    acc = evaluate(model, test_dataloader, device)

    print("评估结果：ACC - ", acc)

if __name__ == '__main__':
    run_evaluate()