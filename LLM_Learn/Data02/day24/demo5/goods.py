
from fastapi import  APIRouter

goods_router = APIRouter(prefix="/goods",tags=["商品模块"])


@goods_router.get("/info")
def info():
    return {"data" : "商品信息"}

@goods_router.get("/orders")
def orders():
    return {"data" : "订单信息"}

@goods_router.get("/count")
def count():
    return {"data" : 100}







