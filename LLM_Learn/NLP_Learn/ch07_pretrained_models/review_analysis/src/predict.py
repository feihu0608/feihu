'''
    推理预测，构建用户程序
'''
import torch

from config import *
from model import ReviewAnalysisModel
from transformers import AutoTokenizer

# 核心方法：输入批量数据 (N, S)，自回归生成，得到预测id列表
def predict_batch(model, inputs, device):
    model.eval()
    # 前向传播
    with torch.no_grad():
        inputs = { k:v.to(device) for k,v in inputs.items() }
        outputs = model(**inputs)
    # 转换为正类概率
    results = torch.sigmoid(outputs)
    return results.tolist()

# 用户预测流程，输入用户文本，返回好评概率
def predict(text, model, tokenizer, device):
    # 1. 编码用户文本
    inputs = tokenizer(
        text,
        padding='max_length',
        max_length=MAX_SEQ_LEN,
        truncation=True,
        return_tensors='pt',
    )

    # 2. 调用预测逻辑，得到预测正类概率（只有一个值）
    result = predict_batch(model, inputs, device)

    return result[0]    # 返回标量值

# 应用程序
def run_predict_app():
    # 1. 定义设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # 2. 获取分词器
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_OR_PATH)

    # 3. 定义并加载模型
    model = ReviewAnalysisModel().to(device)
    model.load_state_dict( torch.load(MODELS_DIR/BEST_MODEL_FILE) )

    print("模型加载成功！")

    print("欢迎使用情感分析程序！输入 q 或者 quit 退出...")

    while True:
        # 等待用户输入中文
        user_input = input("> ")

        if user_input in ['q','quit']:
            print("欢迎下次使用！")
            break

        if user_input.strip() == '':
            print("请输入内容..")
            continue

        result = predict(user_input, model, tokenizer, device)

        if result > 0.5:
            print(f"正向评价: 置信度 {result:.6f}")
        else:
            print(f"负向评价: 置信度 {1-result:.6f}")

if __name__ == '__main__':
    run_predict_app()