# main.py
# 导入FastAPI框架核心、Uvicorn服务器、异常处理类
import uvicorn
from fastapi import FastAPI, Depends, HTTPException

# 导入SQLAlchemy的数据库会话类
from sqlalchemy.orm import Session

# 导入日期类型（如果后续需要处理日期可使用）
from datetime import date

# 导入自动生成的数据库模型类（部门表、员工表）
from models import Departments, Employees

# 导入数据库连接引擎和会话工厂
from database import SessionLocal, engine

# 创建FastAPI应用实例（整个API服务的入口）
app = FastAPI()


# 【核心：数据库依赖项】
# 作用：每次请求时，自动创建一个数据库会话（连接）
# 请求结束后，自动关闭连接，避免资源泄露
def get_db():
    # 创建数据库会话（相当于打开一个数据库连接）
    db = SessionLocal()
    try:
        # yield：把会话对象提供给接口使用
        yield db
    finally:
        # 无论成功失败，最后一定会关闭会话
        db.close()


# ==================== 部门相关 API 接口 ====================

# 接口1：创建新部门（POST请求）
# 路径：/departments/
# 功能：接收前端传来的 name 和 location，存入数据库
@app.post("/departments/")
def create_department(
        name: str,  # 接口参数：部门名称（字符串类型）
        location: str,  # 接口参数：部门位置（字符串类型）
        db: Session = Depends(get_db)  # 自动注入数据库会话
):
    # 1. 创建 Departments 模型对象（对应数据库一行数据）
    db_department = Departments(name=name, location=location)

    # 2. 将对象添加到数据库会话（暂存，未写入磁盘）
    db.add(db_department)

    # 3. 提交事务 → 真正写入数据库
    db.commit()

    # 4. 刷新对象（同步数据库生成的id等字段到Python对象）
    db.refresh(db_department)

    # 5. 返回创建好的部门数据（自动转为JSON）
    return db_department


# 接口2：查询所有部门（GET请求）
# 路径：/departments/
# 功能：返回数据库中所有部门列表
@app.get("/departments/")
def read_departments(db: Session = Depends(get_db)):
    # 查询 Departments 表的所有数据并返回
    return db.query(Departments).all()


# 接口3：根据ID查询单个部门（GET请求）
# 路径：/departments/10
# 功能：根据传入的ID查找对应部门，找不到则返回404
@app.get("/departments/{department_id}")
def read_department(
        department_id: int,  # 路径参数：部门ID（整数类型）
        db: Session = Depends(get_db)
):
    # 根据ID查询部门（filter条件 + first取第一条）
    department = db.query(Departments).filter(Departments.id == department_id).first()

    # 如果没找到，抛出404异常
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    # 返回查询到的部门信息
    return department


# ==================== 启动服务 ====================
if __name__ == "__main__":
    # 直接在Python代码中启动Uvicorn服务器（不用命令行敲指令）
    uvicorn.run(
        app="main:app",  # 固定格式：文件名:FastAPI实例名
        host="0.0.0.0",  # 允许局域网/外部访问
        port=8000,  # 服务端口号
        reload=True  # 开发模式：代码修改后自动重启
    )