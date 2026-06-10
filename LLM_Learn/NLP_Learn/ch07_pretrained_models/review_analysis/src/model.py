'''
    定义模型
'''
from torch import nn
from transformers import AutoModel

from config import *

class ReviewAnalysisModel(nn.Module):
    # 初始化
    def __init__(self):
        super(ReviewAnalysisModel, self).__init__()
        # BERT层
        self.bert = AutoModel.from_pretrained(MODEL_NAME_OR_PATH)
        # 线性层（分类器）
        self.classifier = nn.Linear(in_features=self.bert.config.hidden_size, out_features=1)

    # 前向传播
    def forward(self, input_ids, token_type_ids, attention_mask):
        # 1. BERT前向传播
        outputs = self.bert(input_ids, token_type_ids=token_type_ids, attention_mask=attention_mask)
        # 2. 提取CLS对应的特征向量，(N, 768)
        cls_output = outputs.pooler_output
        # 3. 输出层（分类器）, (N, 1)
        output = self.classifier(cls_output)
        # 压缩一维返回，(N,)
        return output.squeeze(-1)

if __name__ == '__main__':
    model = ReviewAnalysisModel()
    print(model)