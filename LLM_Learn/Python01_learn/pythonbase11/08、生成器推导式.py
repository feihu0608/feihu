from collections.abc import Iterable, Iterator, Generator

gen = (i for i in range(1,101))
print(gen)

# print(next(gen))
for i in gen:
    print(i)


# 生成器推导式和列表推导式，就是括号不一样，其余的都一样
# 但是最终获取数据的本质方式是不一样的
# 列表推导式，一次把所有的数据全部拿到 有可能浪费内存，效率不高
# 生成器推导式，最终我们并没有拿到所有的数据，而是获得一个生成器
# 再去通过生成器一个一个去获取所有的数据，它的内存占用小，效率高

gen1 = (i for i in range(1,101) if i % 2 == 0)
for i in gen1:
    print(i)



# 如何判断可迭代对象、迭代器、生成器

# 生成器是生成器，生成器也是迭代器，生成器还是可迭代对象
print(isinstance(gen1, Iterable))
print(isinstance(gen1, Iterator))
print(isinstance(gen1, Generator))



