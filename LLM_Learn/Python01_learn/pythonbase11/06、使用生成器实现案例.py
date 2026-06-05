
# def oddgenerator():
#     for i in range(1,11,2):
#         yield i
#
# odd_generator = oddgenerator()
#
# # 生成器函数调用返回的是生成器对象
# # 生成器对象和迭代器对象的用法是一样的
#
# print(next(odd_generator))
#
# for i in odd_generator:
#     print(i)




def fibgenerator(n):
    start = 1
    end = n
    a,b = 1,1
    while start <= end:
        result = a
        a,b = b,a+b
        start += 1
        yield result


# 生成器我们是不需要手动去抛异常，一旦条件不成立，自动抛异常，迭代器必须手动抛


fib_generator = fibgenerator(5)
print(next(fib_generator))
print(next(fib_generator))
print(next(fib_generator))
print(next(fib_generator))
print(next(fib_generator))
print(next(fib_generator))









