# 校验装饰器
# user_info = {
#     "username":"yangmi",
#     "password":"111111"
# }
#
# def logingdecorator(func):
#     def wrapper(*args, **kwargs):
#         if user_info["username"] == "yangmi" and user_info["password"] == "123456":
#             result = func(*args, **kwargs)
#             return result
#         else:
#             raise ValueError("用户名或者密码有误")
#     return wrapper
#
#
# @logingdecorator
# def checkout():
#     print("支付的业务逻辑")
#
# checkout()





# 缓存装饰器
list1 = [
    {"id":1,"name":"yangmi","age":18},
    {"id":2,"name":"zhaoliying","age":18},
    {"id":3,"name":"liushishi","age":28},
    {"id":4,"name":"dilireba","age":38},
    {"id":5,"name":"gulinazha","age":48},
]


def cachedecorator(func):
    cache = {}
    # 1: {"id":1,"name":"yangmi","age":18},
    def wrapper(*args,**kwargs):
        if args[0] in cache: #用户的id如果在缓存cache当中
            print("找到了用户，缓存命中了")
            return cache.get(args[0]) #直接返回缓存cache里面的用户数据
        else:
            print("找到了用户，循环遍历找到了")
            result = func(*args,**kwargs)
            cache[args[0]] = result  #代表第一次找，找到的用户结果存入缓存
            return result
    return wrapper


@cachedecorator
def find_star(id):
    for item in list1:
        if item["id"] == id:
            return item
    else:
        return None


print(find_star(1))
print(find_star(2))
print(find_star(3))
print(find_star(1))
print(find_star(2))

