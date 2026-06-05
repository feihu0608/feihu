from fastapi import  APIRouter

user_router = APIRouter(prefix="/user",tags=["用户模块"])


@user_router.get("/info")
def user_info():
    return {"data" "用户信息"}


@user_router.get("/count")
def user_count():
    return {"data" : "用户数量100"}

@user_router.get("/login")
def user_login():
    return {"data" : "用户登录"}

