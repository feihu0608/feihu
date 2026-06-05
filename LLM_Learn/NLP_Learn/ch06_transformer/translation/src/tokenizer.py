"""
    分词器类
"""

from nltk import TreebankWordTokenizer,TreebankWordDetokenizer

from config import *

class BaseTokenizer:
    def __init__(self):
        self.tokenizer = TreebankWordTokenizer()

