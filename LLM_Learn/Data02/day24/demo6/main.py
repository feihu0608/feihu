from base import Base
from database import engine
from insert import insert_data
from delete import delete_data
from update import update_data
from models import Employee , Department

# 创建表
def create_table():
    print("注册的表名:", Base.metadata.tables.keys())
    # 创建所有模型对应的表
    Base.metadata.create_all(bind=engine)
    print("表创建成功")


if __name__ == '__main__':
    # create_table()
    # insert_data()
    # delete_data()
    update_data()
    pass
