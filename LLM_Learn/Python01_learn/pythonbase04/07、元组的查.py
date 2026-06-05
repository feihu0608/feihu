t1 = (1,2,3,4,5)
# 查
# 查单个
print(t1[2])

# 查部分
result = t1[1:4]
print(result,t1) #返回一个新的元组

# 查所有
# 直接查元素
for item in t1:
    print(item)

# 根据下标去查
for i in range(len(t1)):
    print(i,t1[i])

# 直接查下标和元素
for i,item in enumerate(t1):
    print(i,item)


# 函数和方法： 本质都是函数
# 方法一般写法是 a.b()
# 函数一般写法是 a()



# 元组虽然元素不可以改变，但是如果我们要强行进行改变，此时可以先转化为一个列表
# 通过列表修改完成，再把列表转化为一个元组，但是这两个不是同一个元组
# 注意：这句话不是让大家以后直接去强转修改元组，而是不想让大家修改元组
t2 = (1,2,3,4)
# t2[3] = 44
list1 = list(t2)
print(list1)
list1[3] = 44
print(list1)
t4 = tuple(list1)
print(t4)
print(id(t2),id(t4))








