from mcp.client.streamable_http import streamable_http_client
from mcp.client.session import ClientSession

# mcp所有的操作要求必须是异步
async def mcp_streamable_http_run():
    async with streamable_http_client(url="http://localhost:8000/mcp") as (read,write,_):
        async with ClientSession(read,write) as session:
            await session.initialize()
            res = await session.list_tools()
            print(res)
            tool_name = res.tools[0].name
            tool_res = await session.call_tool(tool_name, {"city": "深圳", "date": "2026-06-26"})
            print(tool_res.content[0].text)



if __name__ == '__main__':
    import asyncio
    asyncio.run(mcp_streamable_http_run())

