import asyncio

from langchain.chat_models import init_chat_model

import os
from dotenv import load_dotenv

load_dotenv()
#
# llm = init_chat_model(
#     model = 'Qwen/Qwen3-8b',
#     model_provider = 'openai',
#     base_url = os.getenv("OPENAI_BASE_URL"),
#     api_key = os.getenv("OPENAI_API_KEY"),
#     temperature=0
# )
#
# # messages代表提示词,如果是单条,那么代表一个列表
# # 如果是多条,那么代表一个列表的列表,也就是一个嵌套的列表,就是一个二维列表
#
# messages = [
#     [
#         {"role": 'system', 'content': '你是一个情感分析大师'},
#         {"role": 'user', 'content': '我好无聊啊'}
#     ],
#     [
#         {"role": 'system', 'content': '你是一个情感分析大师'},
#         {"role": 'user', 'content': '给我讲个笑话吧'}
#     ]
# ]
#
# res = llm.batch(messages)
#
# print(type(res))
#
# for r in res:
#     print(r.content)
#
# # langchain的batch批处理,默认是使用多线程的方式,也就是使用了concurrent,futures.ThreadPoolExecutor

# 批处理的异步调用
# langchain中的abatch批处理,使用的协程方式,协程的高并发asyncio.gather(a,b,c)
async def llm_batch_async():

    llm = init_chat_model(
        model='Qwen/Qwen3-8b',
        model_provider='openai',
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0
    )

    # messages代表提示词,如果是单条,那么代表一个列表
    # 如果是多条,那么代表一个列表的列表,也就是一个嵌套的列表,就是一个二维列表

    messages = [
        [
            {"role": 'system', 'content': '你是一个情感分析大师'},
            {"role": 'user', 'content': '我好无聊啊'}
        ],
        [
            {"role": 'system', 'content': '你是一个情感分析大师'},
            {"role": 'user', 'content': '给我讲个笑话吧'}
        ]
    ]

    res = await llm.abatch(messages)

    return res



if __name__ == '__main__':
    res = asyncio.run(llm_batch_async())
    print(type(res))

    for r in res:
        print(r.content)
