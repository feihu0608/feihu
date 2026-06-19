from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage,HumanMessage

from dotenv import load_dotenv

import os

load_dotenv()

llm = init_chat_model(
    model='Qwen/Qwen3-8B',
    model_provider='openai',
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature = 0
)
# 字符串
messages = 'hello'

# 对象列表(HumanMessage,SystemMessage,AiMessage,ToolMessage)
messages = [
    SystemMessage(content="你是一个非常幽默的人"),
    HumanMessage(content="给我讲一个笑话"),
]

# 元祖列表
messages = [
    ("system", "你是一个优秀的翻译官"),
    ("human", "翻译你是一个大聪明"),
]

# 字典列表
messages = [
    {"role":"system","content":"你是一个优秀的翻译官"},
    {"role":"human","content":"翻译今天天气真好"}
]

res = llm.invoke(input=messages)
print(res.content)