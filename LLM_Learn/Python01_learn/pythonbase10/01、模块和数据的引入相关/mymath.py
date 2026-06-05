"""
    自定义模块
"""

list1 = [1,2,3,4]

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    # _remainder(10,30)
    return a/b

def _remainder(a,b): # 为后面演示需要，故意以_开头
    return a%b

# 设置通配符的访问范围
__all__ = ["add","divide","_remainder"]

# if __name__ == '__main__':
#     print(add(10, 20))
#     print(__name__)
