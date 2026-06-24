from langchain.agents import create_agent
from langchain.tools import tool
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

@tool(description="获取某个城市某天的天气状况")
def get_weather(city,date):
    return f'The weather in {city} on {date} will be sunny.'

agent = create_agent(
    model=llm,
    tools=[get_weather]
)

messages = [
    {"role": "user", "content": "深圳在2026年6月28日的天气如何，怎么穿衣服舒服"},
]

# 这里的input传递的时候必须是一个字典，langchain里面封装的，我们只能遵循
res = agent.invoke(input={
    "messages":messages
})

print(res['messages'][-1].content)



# 通过stream打印结果，我们是可以看到调用过程
# res = agent.stream(input={
#     "messages":messages
# })
#
# for r in res:
#     print(r)