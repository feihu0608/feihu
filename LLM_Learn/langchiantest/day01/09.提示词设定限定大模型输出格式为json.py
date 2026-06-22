from typing import List

from langchain.chat_models import init_chat_model
from pydantic import BaseModel
from langchain_core.output_parsers import JsonOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

# 1.把要输出的json格式定义好
# 这个类只是一个格式,他可以是一个字典当中的键值,也可以限定一个对象当中的属性和属性值
class Star(BaseModel):
    name: str
    age: int

class StarList(BaseModel):
    stars: List[Star]

# 2.在提示词的系统提示词当中设置要输出的json格式内容
# 2-1创建一个outputparser
jop = JsonOutputParser(pydantic_object=StarList)

# 2-2在messages中添加一个系统提示词
messages = [
    {"role":'system',"content":"你是一个微博达人"},
    # jop.get_format_instructions()作用等价于你自己写的"请帮我输出json格式,格式必须符合StarList定义的结构"
    {"role":'system',"content":jop.get_format_instructions()},
    {"role":"user","content":"请帮我列出中国最漂亮的三个女明星"},
]


llm = init_chat_model(
    model = 'Qwen/Qwen3-8b',
    model_provider = 'openai',
    base_url = os.getenv('OPENAI_BASE_URL'),
    api_key = os.getenv("OPENAI_API_KEY"),
    temperature = 0,
)

res = llm.invoke(messages)
print(res.content,type(res.content)) # 返回的是json字符串

# 我们把json字符串转换成python当中的字典,反序列化json
result = jop.parse(res.content)
print(result,type(result))

print(result['stars'])
