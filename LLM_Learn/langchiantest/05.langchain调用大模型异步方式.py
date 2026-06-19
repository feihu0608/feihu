import asyncio

from langchain.chat_models import init_chat_model

import os
import dotenv

dotenv.load_dotenv()

async def llm_sync_call():
    llm = init_chat_model(
        model='Qwen/Qwen3-8B',
        model_provider='openai',
        base_url=os.getenv('OPENAI_BASE_URL'),
        api_key=os.getenv('OPENAI_API_KEY'),
        temperature=0
    )

    # llm.invoke() 同步调用放肆
    # 后期我们工作当中几乎用的都是异步调用的方式,效率比同步要高很多

    messages = [
        {"role":"system","content":"你是一个百事通"},
        {"role":"user","content":"请问百度和谷歌哪个更好用"}
    ]

    res = await llm.ainvoke(input=messages)

    return res

if __name__ == '__main__':
    res = asyncio.run(llm_sync_call())
    print(res.content)



