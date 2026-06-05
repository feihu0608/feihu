# 装饰器
def loggerdecorator(func):
    def wrapper(*args, **kwargs):
        print(f"函数的参数是{args}")
        result = func(*args, **kwargs)
        print(f"函数的返回值是{result}")
        return result
    return wrapper


# 装饰器的闭包用法
# 原函数
# def add(a,b):
#     return a + b
# 装饰器的作用：在不改变原函数的功能情况下给原函数添加额外功能
# add = loggerdecorator(add)
# print(add(10, 20))


# 装饰器的用法 @ 本质是把原函数的地址值换成装饰器内层函数的地址
@loggerdecorator  # ===> add = loggerdecorator(add)
def add(a,b):
    return a + b


print(add(10, 20))




# 计时装饰器





# print(sub(10, 20))
import time
def timerdecorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数执行花费了{end_time - start_time}")
        return result
    return wrapper

@timerdecorator
def sub(a,b):
    time.sleep(2)
    return a - b


print(sub(10, 20))











