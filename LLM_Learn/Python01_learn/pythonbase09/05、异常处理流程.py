# a = 100
# print(a)
# result = a / 0
# b = 200
# print(b)
# import traceback
import traceback

try:
    a = 100
    print(a)
    # result = a / 0
    b = 200
    f = open("xxxxx",'r')
    print(b)

    list1 = [1,2,3]
    # print(list1[5])

    # 下面的打印相当于是else里面的内容
    print("如果没有碰到任何异常，所有的except都不会执行")
except ZeroDivisionError as e:
    print("我的处理方案是打印异常信息")
    print(e)

except FileNotFoundError as e:
    # traceback.print_exc()
    print("我的处理方案是打印异常信息")
    print(e)

# except Exception as e:
#     print("我是做异常处理兜底的")
#     print(type(e))
#     print(e)

# else:
#     print("如果没有碰到任何异常，所有的except都不会执行")

finally:
    print("有没有处理异常，都要执行的代码，主要用来做善后处理，比如文件关闭")


# 如果我们不要finally，而是把finally的处理代码写在这，完全是两个意思
# 如果你写的异常没有被处理（没有做兜底，详细异常捕获也没捕获这个异常），此时碰到这个异常，程序就炸了，如果代码没有写在finally当中
# 这段代码就无法执行了，写在finally当中，这段代码一定会执行

# print("有没有处理异常，都要执行的代码，主要用来做善后处理，比如文件关闭")