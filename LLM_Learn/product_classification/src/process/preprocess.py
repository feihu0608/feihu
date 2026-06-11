"""
    数据预处理脚本
"""
from datasets import load_dataset, ClassLabel, Value, Features
from transformers import AutoTokenizer

from common.config import *

def preprocess():
    print("数据预处理开始...")

    # 1. 读取文件，得到数据集字典
    dataset_dict = load_dataset(
        'csv',
        delimiter='\t',
        data_files={
            'train': str(RAW_DATA_DIR/RAW_TRAIN_DATA),
            'valid': str(RAW_DATA_DIR/RAW_VALID_DATA),
            'test': str(RAW_DATA_DIR/RAW_TEST_DATA),
        },
        features=Features({'label':Value('string'),'text_a':Value('string')}), #方法一:类型强转,防止在标签编码那里报错
    )
    # print(dataset_dict)
    # print(dataset_dict['train'][:3])

    # 2. 转换分类标签（标签编码）
    # 2.1 获取训练集中所有的分类标签
    all_labels = sorted( set( dataset_dict['train']['label'] ) )
    print(all_labels)

    # dataset_dict = dataset_dict.cast_column('label', Value("string"))#方法二:类型强转,防止在标签编码那里报错

    # 2.2 标签编码
    class_label = ClassLabel(names=all_labels)
    dataset_dict = dataset_dict.cast_column('label', class_label)
    print(dataset_dict['train'][:3])

    # 保存到文件
    with open(MODELS_DIR/LABELS_FILE,'w',encoding='utf-8') as f:
        f.write('\n'.join(all_labels))

    # 3. 加载分词器
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_OR_PATH)

    # 4. 编码标题文本数据,得到模型输入
    def encode(batch):
        inputs = tokenizer(batch['text_a'],truncation=True)
        inputs['labels'] = batch['label']
        return inputs

    dataset_dict = dataset_dict.map(encode,batched=True,remove_columns=['label','text_a'])

    print(dataset_dict['train'][:3])

    # 5. 保存数据集到文件
    dataset_dict.save_to_disk(PROCESSED_DATA_DIR)

    print("数据预处理完成!")




if __name__ == '__main__':
    preprocess()



