from mcp.server.fastmcp import FastMCP

app = FastMCP(
    port=8000,
)


@app.tool(description="获取某个城市某天的天气状况")
def get_weather(city, date):
    return f'The weather in {city} on {date} will be sunny.'


# transport="stdio",不写默认就是stdio
# stdio和streamable-http区别
# 如果是stdio，那么我们不需要自己手动起这个服务，它是在写客户端的时候执行客户端代码，自动去通过命令启动服务端
# 如果是streamable-http，那么我们需要自己手动去启动服务端，然后再去调用客户端代码


if __name__ == "__main__":
    app.run(
        # transport="stdio",
        transport="streamable-http",
    )