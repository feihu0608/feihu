'''
    配置文件
'''

# 目录
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
MODELS_DIR = ROOT_DIR / 'models'
LOGS_DIR = ROOT_DIR / 'logs'

# 文件
RAW_DATA_FILE = 'online_shopping_10_cats.csv'

# MODEL_NAME_OR_PATH = "google-bert/bert-base-chinese"
MODEL_NAME_OR_PATH = '../../mybert'
BEST_MODEL_FILE = 'best_model.pt'   # 最佳模型参数

# 超参数
LEARNING_RATE = 1e-5
BATCH_SIZE = 16
EPOCHS = 50
MAX_SEQ_LEN = 128