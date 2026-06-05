# 嵌套定义
def fn():
    print("外层函数")
    def fn1():
        print("内层函数")
    fn1()

fn() #执行完，代表fn第一次调用的执行上下文已经销毁了 fn1不在了

# 全局执行上下文当找fn1 fn1不存在 报错
# fn1()




# 嵌套调用
def first_fn():
    print("first_fn start")
    second_fn()
    print("first_fn end")

def second_fn():
    print("second_fn start")
    print("哈哈哈哈")
    print("second_fn end")


first_fn()