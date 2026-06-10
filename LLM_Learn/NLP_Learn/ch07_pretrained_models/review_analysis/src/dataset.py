'''
    构建数据集，创建数据加载器
'''
import torch
from torch.utils.data import DataLoader
from datasets import load_from_disk

from config import *

# 定义获取加载器的方法，训练/测试通用
def get_dataloader(train=True):
    data_file_path = PROCESSED_DATA_DIR / ( 'train' if train else 'test' )
    # 获取数据集
    dataset = load_from_disk(data_file_path)
    dataset.set_format(type='torch')
    # 创建数据加载器
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=train)
    return dataloader

if __name__ == '__main__':
    # 直接获取数据加载器
    train_loader = get_dataloader()
    test_loader = get_dataloader(train=False)
    print("训练集批次数：", len(train_loader))
    print("测试集批次数：", len(test_loader))
    for batch in train_loader:
        for k, v in batch.items():
            print(k, " -> ", v.shape)
        break
    data_iter = iter(test_loader)
    batch = next(data_iter)
    print(batch)