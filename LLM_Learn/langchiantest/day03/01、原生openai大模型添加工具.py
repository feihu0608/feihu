import json

from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()
# 1、定义工具，工具需要有描述信息，我们发给大模型的是描述信息
def get_weather(city,date):
    return f"{city}{date}的天气是晴朗，气温为28℃"


tools = [
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "获取某个城市在特定日期的天气",
      "parameters": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "城市名称, e.g. San Francisco",
          },
          "date" :{
            "type":"string",
            "description":"想要查询的天气的日期, e.g. 2023-12-25"
          }
        },
        "required": ["city","date"],
        "additionalProperties": False,
      },
      "strict": True,
    },
  },
]


# 2、第一次发请求给大模型
messages = [
    {"role":"user","content":"请问深圳2026年6月24日的天气如何，我该如何穿衣服才舒服"}
]

llm = OpenAI(
    base_url=os.getenv('OPENAI_BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY'),
)
res1 = llm.chat.completions.create(
    model="deepseek-ai/DeepSeek-V4-Flash",
    messages=messages,
    tools=tools,
)

print(res1.choices[0].message)

# 3、从大模型返回的工具调用信息当中判断函数名，自己调用工具，同时把返回的调用信息加到messages当中
messages.append(res1.choices[0].message)

tool_call_name = res1.choices[0].message.tool_calls[0].function.name
tool_call_args = res1.choices[0].message.tool_calls[0].function.arguments
tool_call_id = res1.choices[0].message.tool_calls[0].id

# 4、调用工具，同时需要把工具调用的结果添加到messages
if tool_call_name == "get_weather":
    tool_res = get_weather(**json.loads(tool_call_args))
    # 构造工具调用后的消息
    tool_call_message = {
        "tool_call_id":tool_call_id,
        "role":"tool",
        "content":tool_res
    }
    messages.append(tool_call_message)


# 5、第二次发请求给大模型,拿到最终结果
res2 = llm.chat.completions.create(
    model='deepseek-ai/DeepSeek-V4-Flash',
    messages=messages,
    tools=tools,
)

print(res2.choices[0].message.content)










