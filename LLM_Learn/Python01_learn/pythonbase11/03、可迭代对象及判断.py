from collections.abc import Iterable, Iterator, Generator

# list1 = [1,2,3,4,5]
# str1 = "asjdghasdh"
#
# for item in list1:
#     print(item)
# # 本质并不是遍历列表本身 而是在遍历列表的迭代器
#
# # 拿到迭代对象身上的迭代器
# print(list1.__iter__())
# print(iter(list1))
#
# for item in iter(list1):
#     print(item)

# for循环遍历可迭代对象其实是一个语法糖
# 遍历可迭代对象的本质其实是在遍历迭代器


# print(iter(100))

#可迭代对象的判断
list1 = [1,2,3]
print(isinstance(list1,Iterable))
print(isinstance(list1,Iterator))
print(isinstance(list1,Generator))

str1 = 'asuidghasd'
print(isinstance(str1,Iterable))
print(isinstance(100,Iterable))

# 一个可迭代对象身上一定有迭代器
# 可迭代对象不一定是迭代器
# 迭代器一定是可迭代对象
# 迭代器身上也有迭代器（就是自己）


# 可迭代对象是可迭代对象
# 可迭代对象不一定是迭代器
# 可迭代对象不一定是生成器
