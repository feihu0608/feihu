"""
    第一个web项目
    HTTP 请求的类型
        get 在浏览器的地址栏发送的请求 都属于get请求
        post 必须通过表单或者一些测试框架swagger才可以发送
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "欢迎访问我的第一个网站"}  # python中我们称之为字典 在前端称之为 JSON格式的字符串


@app.get("/get_goods_info")
def get_goods_info():
    return {"1" : "商品1" , "2" : "商品2"}