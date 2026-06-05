def add(a,b):
    return a + b

# 函数和普通数据一样
a = add
print(a(10, 20))


# 函数当参数
def fn(func):
    return func(10,20)


print(fn(a))


# 函数当返回值（闭包的雏形 装饰器的雏形）
def fn1():
    def fn2(a,b):
        return a + b
    return fn2


print(fn1()(10, 20))
