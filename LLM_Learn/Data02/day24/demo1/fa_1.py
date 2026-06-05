"""
    回顾之前的普通函数执行 进栈 先进后出 FILO
"""


def func2():
    print("函数2开始执行")
    print("函数2执行完毕")


def func1():
    print("函数1开始执行")
    func2()
    print("函数1执行完毕")


func1()