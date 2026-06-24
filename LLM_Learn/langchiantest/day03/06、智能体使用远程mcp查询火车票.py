from langchain.agents import create_agent
# 使用模搭的mcp广场线上工具
from langchain_mcp_adapters.client import MultiServerMCPClient

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

async def mcp_12306_run():
    client = MultiServerMCPClient(
        {
            "12306": {
                "transport": "streamable_http",
                "url": "https://mcp.api-inference.modelscope.net/ed0440b77af349/mcp"
            }
        }
    )
    tools = await client.get_tools()
    # print(tools)

    agent = create_agent(
        model=llm,
        tools=tools,
    )


    messages = [
        {"role": "user", "content": "请帮我查询一下从北京到上海2026年6月24日的高铁票，越详细越好，最后以列表的形式给我展示"},
    ]
    res = await agent.ainvoke(
        input={
            "messages":messages
        }
    )
    print(res['messages'][-1].content)





if __name__ == "__main__":
    import asyncio
    asyncio.run(mcp_12306_run())