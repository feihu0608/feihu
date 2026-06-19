from typing import List

from langchain.chat_models import init_chat_model
from pydantic import BaseModel

import os
from dotenv import load_dotenv

load_dotenv()

class Star(BaseModel):
    name: str
    age: int

class StarsList(BaseModel):
    stars: List[Star]

messages = [
     {"role":'system',"content":'你是一个头条总结大师'},
     {"role":'human','content':'请帮我列出全球最漂亮的三个女明星'}
]

llm = init_chat_model(
    model = 'deepseek-ai/DeepSeek-V4-Flash',
    model_provider='openai',
    base_url = os.getenv('OPENAI_BASE_URL'),
    api_key = os.getenv('OPENAI_API_KEY'),
    temperature = 0,
)
# 设定工具,制定结构化输出
new_llm = llm.with_structured_output(StarsList)

res = new_llm.invoke(messages)

print(res,type(res))

print(res.stars)



