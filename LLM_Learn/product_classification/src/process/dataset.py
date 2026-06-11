"""
    获取数据集和数据加载器
"""
from datasets import load_from_disk
from torch.utils.data import DataLoader
from transformers import AutoTokenizer,DataCollatorWithPadding

from common.config import *

# 获取数据集,传入数据集的类型
def get_dataset(ds_type = 'train'):
    # 加载数据集
    path = str(PROCESSED_DATA_DIR/ds_type)
    dataset = load_from_disk(path)
    return dataset

# 获取加载器,传入数据集的类型
def get_dataloader(tokenizer, ds_type = 'train'):
    dataset = get_dataset(ds_type)

    dataset.set_format(type='torch')

    # 创建加载器
    collate_fn = DataCollatorWithPadding(
        tokenizer=tokenizer,
        padding=True,
        return_tensors='pt'
    )

    dataloader = DataLoader(dataset,batch_size=BATCH_SIZE,shuffle=True,collate_fn=collate_fn)
    return dataloader
if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_OR_PATH)
    dataloader = get_dataloader(tokenizer)

    for batch in dataloader:
        print(batch)
        for k,v in batch.items():
            print(k,'->',v)
        break


