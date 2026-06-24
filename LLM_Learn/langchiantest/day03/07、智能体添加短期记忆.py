from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
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
# 添加记忆
# 1、checkpointer赋值
# 2、每次执行的时候让配置当中配置相同的thread_id

agent = create_agent(
    model=llm,
    checkpointer=InMemorySaver()
)

messages = [
    {"role": "user", "content": "langchain是什么？"},
]

res = agent.invoke(input={
    "messages":messages
},config={
    "configurable":{
        "thread_id":1
    }
})

print(res['messages'][-1].content)



messages1 = [
    {"role": "user", "content": "我刚才问了你什么"},
]
res1 = agent.invoke({
    "messages":messages1
},config={
    "configurable":{
        "thread_id":1
    }
})

print(res1['messages'][-1].content)


# 一句话：把上面的配置配置ok后，执行两次看看第二次能不能知道第一次问了什么，如果能就是添加短期记忆了，不能就是没有
