"""
    定义数据结构
"""
from pydantic import BaseModel

# 商品类
class Item(BaseModel):
    title: str



