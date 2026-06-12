"""
    配置文件
"""
from pathlib import Path

# 1. 目录路径
ROOT_DIR = Path(__file__).parents[2]

DATA_DIR = ROOT_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'

MODELS_DIR = ROOT_DIR / 'models'
LOGS_DIR = ROOT_DIR / 'logs'

# 2. 文件名
RAW_TRAIN_DATA = 'train.txt'
RAW_TEST_DATA = 'test.txt'
RAW_VALID_DATA = 'valid.txt'

MODEL_NAME_OR_PATH = 'google-bert/bert-base-chinese'
LABELS_FILE = 'labels.txt'

# 3. 训练超参数
BATCH_SIZE = 32
EPOCHS = 10
LEARNING_RATE = 1e-5

SAVE_STEPS = 100    # 判断模型保存的频次（迭代批次数）



