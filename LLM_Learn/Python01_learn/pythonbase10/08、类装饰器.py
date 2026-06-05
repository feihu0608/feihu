
# 把前面的日志装饰器改为类实现
# 1、类里面的构造方法 init  里面去保存原函数
# 2、我们要去添加的功能使用 call,里面去调用原函数添加额外功能即可
class LoggerDecorator:
    def __init__(self, func):
        self.func = func

    # call是把一个实例对象，当做函数去用的时候自动调用  实例化对象() 就是把实例当函数用
    def __call__(self, *args, **kwargs):
        print(f"函数的入参信息是{args}")
        result = self.func(*args, **kwargs)
        print(f"函数的返回值是{result}")
        return result


@LoggerDecorator # ==》 add = LoggerDecorator(add) ==> add = LoggerDecorator类的实例化对象
def add(a,b):
    return a+b


print(add(10, 20))







