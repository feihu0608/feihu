from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model = 'Qwen/Qwen3-8b',
    model_provider = 'openai',
    base_url = os.getenv('OPENAI_BASE_URL'),
    api_key = os.getenv('OPENAI_API_KEY'),
    temperature = 0,
)

message = [
    {"role":'system','content':'你是一个{job}'},
    {"role":'human','content':'我想问{question}'}
]
# 可以不写from_messages直接调用构造方法__init__进行传入,推荐使用from_messages,ChatPromptTemplate(messages) 和 ChatPromptTemplate.from_messages(messages) 底层做的事情几乎完全一样，只是 from_messages 提供了更丰富的输入格式支持和更好的语义表达。
cpt = ChatPromptTemplate.from_messages(message)

message1 = cpt.invoke({'job':'情感分析大师','question':'不开心怎么办?'})

res = llm.invoke(message1)

print(res.content)




