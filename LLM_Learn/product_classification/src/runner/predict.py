"""
    预测脚本
"""
import torch
from transformers import AutoTokenizer,AutoModelForSequenceClassification

from common.config import *

# 预测器
class Predictor():
    def __init__(self,model,tokenizer,device):
        self.model = model.to(device)
        self.tokenizer = tokenizer
        self.device = device

    # 核心方法: 传入一批文本,预测分类标签,返回列表
    def predict(self,text : str | list[str]):
        # 判断输入类型,统一成列表形式
        is_str = isinstance(text,str)
        if is_str:
            text = [text]

        # 1. 分词编码,得到模型输入
        inputs = self.tokenizer(
            text,
            padding=True,
            truncation=True,
            return_tensors="pt",
        )

        input_ids = { k: v.to(self.device) for k, v in inputs.items() }

        # 2. 模型前向传播,得到预测输出
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(**input_ids)

        # 3. 将输出转换为分类标签
        pred_labels = torch.argmax(outputs.logits,dim=-1).tolist()
        results = [ self.model.config.id2label[label_id] for label_id in pred_labels ]

        # 4. 如果是一条数据,获取第一个元素返回
        if is_str:
            return results[0]
        return results

def predict():
    # 1. 定义设备
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 2. 加载分词器
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_OR_PATH)

    # 3. 加载模型
    model = AutoModelForSequenceClassification.from_pretrained(MODELS_DIR / 'best')

    # 4. 创建预测器
    predictor = Predictor(model,tokenizer,device)

    # 5. 预测
    text = '好奇心钻装纸尿裤L40片9-14kg'
    result = predictor.predict(text)
    print("预测结果：", result)

    texts = ['瓦伦丁Wurenbacher小麦西柚啤酒500ml*12听整箱装德国原装进口果啤', '911-267遥控车', '125ML*4伊利臻浓牛奶']
    results = predictor.predict(texts)
    print("预测结果：", results)


if __name__ == '__main__':
    predict()




