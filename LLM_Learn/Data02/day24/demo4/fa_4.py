"""
    参数顺序的问题
    如果路径包含相同的层级目录 注意书写顺序 否则会前边的函数处理路径
    覆盖了后续的函数
"""

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class Student(BaseModel):
    name : str
    age : int
    class_room : str | None = None



app = FastAPI()


@app.get("/")
def root():
    return {"msg": "欢迎访问我的第一个网站"}  # python中我们称之为字典 在前端称之为 JSON格式的字符串



@app.post("/add_student")
def add_student(student: Student):
    return {"msg" : "学生添加成功" , "data" : student}



if __name__ == "__main__":
    uvicorn.run(app="fa_4:app",host="0.0.0.0",port=8000,reload=True)




