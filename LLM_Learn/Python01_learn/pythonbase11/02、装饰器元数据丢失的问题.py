from functools import wraps
def loggerdecorator(func):
    print("我爱你杨幂")
    @wraps(func)  #帮你把元数据恢复
    def wrapper(*args, **kwargs):
        print(f"函数的入参信息是{args}")
        result = func(*args, **kwargs)
        print(f"函数的返回值是{result}")
        return result
    return wrapper

@loggerdecorator
def add(a,b):
    return a+b

# 元数据 我们可以这样打印
# 不用装饰器 原函数名字是add
# 用了装饰器，原函数再去打印的时候名字是wrapper 其实本身就应该是wrapper，但是对于客户来说元数据和调用的函数数据不匹配
# 所以我们可以强制把元数据再给改回来，但是功能不变
print(add.__name__)




