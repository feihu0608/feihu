
# 1、先把装饰器写好
# 2、在装饰器外面再套一层函数专门用于接受参数
# 3、外部函数返回装饰器
def loggerlevel(level="INFO"):
    def loggerdecorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}]函数的入参信息是{args}")
            result = func(*args, **kwargs)
            print(f"[{level}]函数的返回值是{result}")
            return result
        return wrapper
    return loggerdecorator

@loggerlevel(level="ERROR") # ===> @loggerdecorator ==> add = loggerdecorator(add)
def add(a,b):
    return a + b


print(add(10, 20))
