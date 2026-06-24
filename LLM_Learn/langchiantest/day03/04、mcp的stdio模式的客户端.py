from mcp.client.stdio import stdio_client,StdioServerParameters
from mcp.client.session import ClientSession

# mcp所有的操作要求必须是异步
async def mcp_stdio_run():
    # 启动stdio模式的服务端
    server_params = StdioServerParameters(
        command="../.venv/Scripts/python.exe",
        args=["./mcpserver.py"],
    )
    # 创建客户端和服务端的连接
    async with stdio_client(server_params) as (read, write):
#         创建和服务器的链接后，要再去创建会话
        async with ClientSession(read, write) as session:
            # 会话创建完成，首先得先初始化
            await session.initialize()
            res = await session.list_tools()
            print(res)
            tool_name = res.tools[0].name
            tool_res = await session.call_tool(tool_name,{"city":"深圳","date":"2026-06-25"})
            print(tool_res.content[0].text)


if __name__ == '__main__':
    import asyncio
    asyncio.run(mcp_stdio_run())

