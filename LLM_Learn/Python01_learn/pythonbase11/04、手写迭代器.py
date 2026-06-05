# # 自己手写的迭代器，你可以安心的去惰性生成
#
# # 1到100的技术
#
# class OddIterator(object):
#     def __init__(self, n):
#         self.start = 1
#         self.end = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
# #         惰性生成的逻辑
#         result = self.start
#         if result > self.end:
#             raise StopIteration #手动抛出异常
#         self.start += 2
#         return result
#
# odd_iterator = OddIterator(10)
# print(odd_iterator)
#
# # 1、迭代器可以让你调用next方法 一个一个拿
# print(odd_iterator.__next__(),'调用next一个一个获取')
# print(odd_iterator.__next__(),'调用next一个一个获取')
# # print(odd_iterator.__next__())
# # print(odd_iterator.__next__())
# # print(odd_iterator.__next__())
# # print(next(odd_iterator))
#
#
#
#
# # 2、可以遍历迭代器，全部一个一个拿出来
# # 本质其实是在遍历迭代器，遍历一次调用next(odd_iterator)
# # 把所有的数据给你生成，并且会忽略最后的异常
# for i in odd_iterator:
#     print(i)
#
#
#
# # 迭代器在使用的时候不可逆
from collections.abc import Iterator, Iterable, Generator


# 实现一个迭代器惰性生成斐波那契

class FibIterator:
    def __init__(self, n):
        self.start = 1
        self.end = n
        self.a, self.b = 1, 1  #(a代表当前月的兔子对数)

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        if self.start > self.end:
            raise StopIteration
        self.start += 1
        self.a, self.b = self.b, self.a + self.b
        return result


fib_iterator = FibIterator(5)
# print(next(fib_iterator))
# print(next(fib_iterator))
# print(next(fib_iterator))
# print(next(fib_iterator))
# print(next(fib_iterator))
# print(next(fib_iterator))

for i in fib_iterator:
    print(i)


# 迭代器是迭代器
# 迭代器也是可迭代对象
# 迭代器不一定是生成器

print(isinstance(fib_iterator, Iterable))
print(isinstance(fib_iterator, Iterator))
print(isinstance(fib_iterator, Generator))







