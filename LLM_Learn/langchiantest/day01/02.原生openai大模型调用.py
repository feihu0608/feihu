

from openai import OpenAI
import os
import logging
logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv

load_dotenv()

# 创建大模型
llm = OpenAI(
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY'),
)

# 书写消息(问的问题)
messages = [
    {"role":"system","content":"你是一个专业的翻译官"},
    {"role":"user","content":"请翻译一下:我爱你"}
]

# 掉用大模型传递问题
res = llm.chat.completions.create(
    model='Qwen/Qwen3-8B',
    messages = messages
)

# print(res)
# # 打印返回的响应内容
print(res.choices[0].message.content)

# 只要是调用大模型，本质在背后一定是在发请求（http）


