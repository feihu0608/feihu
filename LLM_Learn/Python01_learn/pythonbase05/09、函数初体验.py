# print("程序开始")
# a = 100
# print(a)
#
# for i in range(100):
#     print("我爱你赵丽颖")
#
# b = 200
# print(b)
#
#
#
# for i in range(100):
#     print("我爱你赵丽颖")
#
# c = 300
# print(c)
#
#
# for i in range(100):
#     print("我爱你赵丽颖")


# 函数定义 本质就是定义了一个变量，变量里面放了函数数据的地址  print_love函数变量
def print_love():
    for i in range(100):
        print("我爱你赵丽颖")


print("程序开始")
a = 100
print(a)

print_love() #函数调用 全称叫函数调用表达式

b = 200
print(b)

print_love()

c = 300
print(c)

print_love()


