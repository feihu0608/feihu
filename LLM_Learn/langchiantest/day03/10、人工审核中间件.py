from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()
import os

llm = init_chat_model(
    model='deepseek-ai/DeepSeek-V4-Pro',
    model_provider='openai',
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0
)

@tool(description="获取某个城市某个日期的天气")
def get_weather(city,date):
    return f"{city}{date}的天气是晴朗"


@tool(description="给某人转账")
def transfer_money(name,money):
    return f"给{name}转账{money}元"



hm = HumanInTheLoopMiddleware(
    interrupt_on={
        "get_weather":False,
        "transfer_money":True,#打断审核
    }
)


agent = create_agent(
    model=llm,
    middleware=[hm],
    tools=[transfer_money,get_weather],
    checkpointer=InMemorySaver()
)

messages = [
    {"role": "user", "content": "深圳2026-06-29的天气如何,如何穿衣服"},
]

res = agent.invoke(input={
    "messages":messages
},config={
    "configurable":{
        "thread_id":2
    }
})

print(res)


messages1 = [
    {"role": "user", "content": "请给杨幂转账1000000，告诉我爱她"},
]

res1 = agent.invoke(input={
    "messages":messages1
},config={
    "configurable":{
        "thread_id":100
    }
})

if '__interrupt__' in res1:
# #     人工审核通过
#     command = Command(
#         resume={
#             "decisions": [
#                 {
#                     "type": "approve",
#                 }
#             ]
#         }
#     )

#     人工审核拒绝
#     command = Command(
#         # Decisions are provided as a list, one per action under review.
#         # The order of decisions must match the order of actions
#         # in the interrupt request.
#         resume={
#             "decisions": [
#                 {
#                     "type": "reject",
#                     # Optional: explain why the action was rejected
#                     # and whether the agent should retry a different approach.
#                     "message": "User rejected this action. Do not retry this tool call.",
#                 }
#             ]
#         }
#     )

    # 人工审核修改
    command = Command(
        # Decisions are provided as a list, one per action under review.
        # The order of decisions must match the order of actions
        # in the interrupt request.
        resume={
            "decisions": [
                {
                    "type": "edit",
                    # Edited action with tool name and args
                    "edited_action": {
                        # Tool name to call.
                        # Will usually be the same as the original action.
                        "name": "transfer_money",
                        # Arguments to pass to the tool.
                        "args": {"name": "赵丽颖", "money": 100},
                    }
                }
            ]
        }
    )


    res2 = agent.invoke(input=command,config={
        "configurable":{
            "thread_id":100
        }
    })
    print(res2)








