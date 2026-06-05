import time
def loggerdecorator(func):
    print("我爱你杨幂")
    def wrapper(*args, **kwargs):
        print(f"函数的入参信息是{args}")
        result = func(*args, **kwargs)
        print(f"函数的返回值是{result}")
        return result
    return wrapper


def timerdecorator(func):
    print("我爱你赵丽颖")
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数执行的耗时是{end_time - start_time}")
        return result
    return wrapper


# 装饰器是什么时候执行的？
# 原函数在定义的时候，装饰器就执行了

# 装饰器执行的顺序是什么
# 从下往上，离函数越近越先走

@loggerdecorator
@timerdecorator
def add(a,b):
    return a+b


print(add(10, 20))



