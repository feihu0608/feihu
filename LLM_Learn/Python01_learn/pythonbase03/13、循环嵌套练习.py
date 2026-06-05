# 循环嵌套练习
# 一个循环当中又出现循环


# 打印图形：

# 一定是双层循环，外层循环控制行（打印几行），内层循环控制列（打印几个星）
# 双层循环一定要清楚，外层循环走一次，内层循环走一轮

# 打印矩形 5*5 一次打印一颗星
for i in range(5):
    for j in range(5):
        print("*",end='')
    print('')


# 打印直角三角形
for i in range(10):
    for j in range(i + 1):
        print("*", end='')
    print('')


# 打印等腰三角形
for i in range(5):
    for j in range(4 - i):
#         空格
        print(" ",end="")
    for k in range(2 * i + 1):
        # 打星星
        print("*",end="")
#   换行
    print("")


# 打印乘法口诀表
for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{j} * {i} = {i * j}",end="\t")
    print('')














