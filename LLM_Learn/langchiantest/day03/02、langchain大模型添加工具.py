# langchain最大的贡献就是把工具描述给简化掉了
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langchain.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
# 1、定义工具和描述
@tool(description="获取某个城市在特定日期的天气") #函数当中可以不写函数说明
# @Tool #函数当中必须写函数说明
def get_weather(city,date):
    return f"{city}{date}的天气是晴朗，气温为28℃"


messages = [
    {"role":"user","content":"请问深圳2026年6月24日的天气如何，我该如何穿衣服才舒服"}
]

llm = init_chat_model(
    model="deepseek-ai/DeepSeek-V4-Flash",
    model_provider="openai",
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY'),
    temperature=0
)

# 添加工具，调用一个方法
new_llm = llm.bind_tools([get_weather])
# 第一次发请求给大模型
res = new_llm.invoke(input=messages)
# print(res)
messages.append(res)

tool_call_name = res.tool_calls[0]['name']
tool_call_args = res.tool_calls[0]['args']
tool_call_id = res.tool_calls[0]['id']

if tool_call_name == "get_weather":
    # 调用工具
    tool_res = get_weather.invoke(tool_call_args)
    # 下面工造工具调用的信息，可以是字典也可以用BaseMessage对象
    tool_call_message = ToolMessage(
        content=tool_res,
        tool_call_id=tool_call_id,
    )
    messages.append(tool_call_message)

# 第二次发请求给大模型
res2 = new_llm.invoke(input=messages)
print(res2.content)
