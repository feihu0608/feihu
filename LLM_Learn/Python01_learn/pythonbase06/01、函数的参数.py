# 形参
# 形参全称叫形式参数
# 写的位置在函数定义的小括号当中，本质其实相当于是在函数内部定义的变量
#
# 实参
# 实参全称叫实际参数
# 写的位置在函数调用的小括号当中，本质相当于是给形参赋的值，实参都是值
# 实参的值要赋给形参，本质是把这个值的地址给形参
#
# 形参实参的关系就像你定义了一个变量赋值
# a(形参) = 100(实参)
#
# 传参本质
# 把实参地址值传递给形参变量存储

# 为啥要有参数？参数可以让函数功能更灵活

# 函数只是一个功能，要想这个功能强大灵活，参数可以做到
# 下面这个函数写死了，函数功能就被限制了
# def print_love():
#     for i in range(10):
#         print("我爱你杨幂")
#
# print_love()


#案例：
# 函数一旦有参数，那么灵活度就上升
def print_love(n,name):
    for i in range(n):
        print(f"我爱你{name}")

print_love(10,'杨幂')


a = 100
b = 200

print_love(100,"赵丽颖")





#打印n*n的矩形

def print_rectangle(row,col):
    for i in range(row):
        for j in range(col):
            print("*",end="")
        print("")

print_rectangle(8,10)











