# 一个函数在执行的时候内部自己调用自己
# 直接递归
# A函数执行的时候调用B函数，B函数内部又调A函数
# 间接递归
#
# 一个正常安全的递归调用需要满足以下条件
# 1、具有明确的结束条件
# 2、每次递归调用都要有趋近于结束条件的趋势
#
# 递归虽然代码简洁，但是能不用则不用，因为递归消耗资源大，效率低
#
# 案例：阶乘
# n! = (n-1)! * n
# mul = 1
# for i in range(1,11):
#     mul *= i

def factorial(n):
    # 明确结束条件
    if n <= 0:
        return 1

    return n * factorial(n-1) #趋势

print(factorial(5))
# 后期我们在使用函数实现递归的时候主要是找规律




# 案例：斐波那契（兔子）
# 兔子数列： 一对农夫去买了一对兔子，兔子隔一个月之后，每个月都会生一对新兔子，问农夫第n个月有多少对兔子
def fibonacci(n):
    if n <= 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))






