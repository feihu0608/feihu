'''
    数据预处理脚本：生成处理之后的数据文件（以及词表文件）
'''
from datasets import load_dataset, ClassLabel
from transformers import AutoTokenizer

from config import *

def preprocess():
    print("数据预处理开始...")

    # 1. 读取文件
    dataset = load_dataset('csv', data_files=str(RAW_DATA_DIR/RAW_DATA_FILE))['train']
    print(dataset)

    # 2. 数据清洗
    dataset = dataset.remove_columns(['cat'])
    dataset = dataset.filter(lambda x: x['review'] is not None)
    print(dataset)

    # 3. 划分数据集
    dataset = dataset.cast_column('label', ClassLabel(names=['neg', 'pos']))
    dataset_dict = dataset.train_test_split(test_size=0.2, stratify_by_column='label')
    print(dataset_dict)

    # 4. 创建分词器
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_OR_PATH)

    # 5. 编码数据，生成训练集和测试集
    # 定义编码函数
    def encode(batch):
        inputs = tokenizer(
            batch['review'],
            padding='max_length',
            max_length=MAX_SEQ_LEN,
            truncation=True,
            # return_tensors='pt',
        )
        inputs['labels'] = batch['label']
        return inputs

    dataset_dict = dataset_dict.map(encode, batched=True, remove_columns=['review', 'label'])
    print(dataset_dict)

    # 6. 保存数据集
    dataset_dict.save_to_disk(PROCESSED_DATA_DIR)

    print("数据预处理完成！")

if __name__ == '__main__':
    preprocess()