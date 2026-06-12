import torch
from fastapi import FastAPI
from transformers import AutoTokenizer,AutoModelForSequenceClassification

from common.config import *
from runner.predict import Predictor
from web.schema import Item
from web.service import TitleService

app = FastAPI()

# 创建一个预测器
# 1. 定义设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 2. 加载分词器
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_OR_PATH)

# 3. 加载模型
model = AutoModelForSequenceClassification.from_pretrained(MODELS_DIR / 'best')

# 4. 创建预测器
predictor = Predictor(model=model, tokenizer=tokenizer, device=device)

# 5. 创建标题预测服务
service = TitleService(predictor=predictor)


@app.post("/predict")
def predict(item:Item):
    label = service.predict(item.title)
    return {"商品标题": item.title,"类目": label}

import uvicorn

def run_app():
    uvicorn.run("web.web_app:app", host="0.0.0.0", port=8880, reload=True)
