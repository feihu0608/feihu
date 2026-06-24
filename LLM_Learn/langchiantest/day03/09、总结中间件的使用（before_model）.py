from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from pyexpat.errors import messages

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

sm = SummarizationMiddleware(
    model=llm,
    trigger=[("messages", 2)],  #历史消息达到2条，触发总结
    keep=("messages", 4),#保留最近的4条原始（没有总结的）历史消息，后面的才做总结
)

agent = create_agent(
    model=llm,
    middleware=[sm],
    checkpointer=InMemorySaver()
)

messages = [
    {"role": "user", "content": "langchain是什么？"},
]

res = agent.invoke(input={
    "messages": messages,
},config={
    "configurable":{
        "thread_id":100
    }
})

print(res)



messages1 = [
    {"role": "user", "content": "langgraph是什么？"},
]

res1 = agent.invoke(input={
    "messages": messages1,
},config={
    "configurable":{
        "thread_id":100
    }
})

print(res1)


messages2 = [
    {"role": "user", "content": "杨幂家在哪里？"},
]

res2 = agent.invoke(input={
    "messages": messages2,
},config={
    "configurable":{
        "thread_id":100
    }
})

print(res2)

# 总结中间件必须要使用记忆
# 1、添加记忆之后，后面的消息会包含之前提问返回的消息
# 2、我们在设置总结触发条件的时候是trigger和keep一起作用的，我们遵循的宗旨就是看返回的条数，来去设定这个值，
# 偶数就设置2的倍数，奇数我们就要算一个适当的值