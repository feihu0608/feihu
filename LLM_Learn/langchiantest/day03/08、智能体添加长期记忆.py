from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
# 添加记忆
# 1、checkpointer赋值
# 2、每次执行的时候让配置当中配置相同的thread_id

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()
import os

llm = init_chat_model(
    model='deepseek-ai/DeepSeek-V4-Flash',
    model_provider='openai',
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0
)

import sqlite3
conn = sqlite3.connect(database="./test.db",check_same_thread=False)
agent = create_agent(
    model=llm,
    checkpointer=SqliteSaver(conn=conn)
)

# messages = [
#     {"role": "user", "content": "langchain是什么？"},
# ]
messages = [
    {"role": "user", "content": "我刚才问了你什么？"},
]


res = agent.invoke(input={
    "messages":messages
},config={
    "configurable":{
        "thread_id":1
    }
})

print(res['messages'][-1].content)


