"""
    配置文件
"""

# 目录
from pathlib import Path

ROOT_DIR = Path(__file__).parents[1] # 向上两级目录
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = ROOT_DIR / "models"
LOGS_DIR = ROOT_DIR / "logs"

# 文件
RAW_DATA_FILE = 'cmn.txt'
TRAIN_DATA_FILE = 'train.jsonl'
TEST_DATA_FILE = 'test.jsonl'

EN_VOCAB_FILE = 'en_vocab.txt'  # 词表文件
ZH_VOCAB_FILE = 'zh_vocab.txt'

BEST_MODEL_FILE = 'best_model.pt'   # 最佳模型参数

# 特殊token
UNK_TOKEN = '<unk>'
PAD_TOKEN = '<pad>'
SOS_TOKEN = '<sos>'
EOS_TOKEN = '<eos>'

# 超参数
LEARNING_RATE = 1e-3
BATCH_SIZE = 64
EPOCHS = 50
MAX_SEQ_LEN = 128

D_MODEL = 128
NUM_HEADS = 4
NUM_ENCODER_LAYERS = 2