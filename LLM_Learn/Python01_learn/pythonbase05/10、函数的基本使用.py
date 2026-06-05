# for i in range(1,100):
#     if i % 3 == 0:
#         print(i)
#

def print_divition():
    for i in range(1, 100):
        if i % 3 == 0:
            print(i)


print(print_divition) #函数本质就是个数据，地址值存储在函数名变量当中

# 函数调用

result = print_divition() #函数调用 本质是一个表达式，表达式的特点有值，函数的返回值就是它的值，如果没有返回值结果就是None
print(result)








