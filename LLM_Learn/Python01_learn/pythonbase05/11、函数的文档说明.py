
# 定义 函数在函数内部一开始写函数的文档说明

def add(a,b):
    """
    :功能 : 相加
    :param a: 一个数
    :param b: 另一个数
    :return:  返回值
    """
    return a + b


result = add(10,20)
print(result)

print(help(add))  #打印函数的文档说明信息
