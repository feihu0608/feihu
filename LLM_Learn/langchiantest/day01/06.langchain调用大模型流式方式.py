from langchain.chat_models import init_chat_model


import os
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model='Qwen/Qwen3-8B',
    model_provider='openai',
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('openai_api_key'),
    temperature=0,
)

messages = [
    {"role":"system","content":'你是一个非常优秀的情感分析大师'},
    {"role":"human","content":"宝宝你不要走啊"}
]

res = llm.stream(messages)

print(type(res))

for r in res:
    print(r.content,end='')




