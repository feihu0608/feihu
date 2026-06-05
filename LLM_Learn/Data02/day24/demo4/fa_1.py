"""
    第一个web项目
    HTTP 请求的类型
        get 在浏览器的地址栏发送的请求 都属于get请求
        post 必须通过表单或者一些测试框架swagger才可以发送
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "欢迎访问我的第一个网站"}  # python中我们称之为字典 在前端称之为 JSON格式的字符串


@app.get("/items/{data}")
# 对于items/{data} data属于路径参数  如果我们在函数中指定了参数的数据类型 FastAPI会自动做数据的类型转换
# 对于没有在访问路径中书写的参数 属于查询参数 查询参数需要在浏览器地址栏中 通过?的方式进行拼接传入
def items(data:int, q:str | None = None):
    return {"data": data, "q": q}

if __name__ == "__main__":
    # app 指定运行的程序
    # host 可以访问的主机 如果指定为 127.0.0.1 表示只能本机访问 0.0.0.0 表示局域网内都可以访问
    # port 端口号
    # reload = True 表示热加载 热部署 即修改代码以后不需要重启服务器(不是很好用)
    uvicorn.run(app="fa_1:app",host="0.0.0.0",port=8000,reload=True)




