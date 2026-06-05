list1 = [1,2,3,4,5]
print(list1,type(list1))

#1、 列表的查
# 1-1根据下标索引（查单个）
print(list1[0],list1[1],list1[2])
# 1-2切片(查部分)
# list[起始位置:结束位置:步长]

list2 = list1[::2] #复制一个列表新的
print(list2,type(list2),id(list2),id(list1))
list3 = list1[:3] #起始位置如果不写默认从0开始
print(list3,type(list3),id(list3),id(list1))
list4 = list1[2:] #结束位置不写默认拿到最后
print(list4,type(list4),id(list4),id(list1))
list5 = list1[1:4]
print(list5,type(list5),id(list5),id(list1))

# 切片可以写负数 序列从后往前默认下标从-1开始
# 如果没有步长，那么切片永远都是从左往右去切
list6 = list1[-1:]
print(list6,type(list6),id(list6),id(list1))
list7 = list1[:-3]
print(list7,type(list7),id(list7),id(list1))
list8 = list1[-4:-2]
print(list8,type(list8),id(list8),id(list1))

# 如果步长为负数，那么就是从右往左切
list9 = list1[::-1]
print(list9,type(list9),id(list9),id(list1))
# list10 = list1[-2:-5:-1]
list10 = list1[3:0:]
print(list10,type(list10),id(list10),id(list1))

# 总结：切片的时候，下标有两种表示  正数和负数，但是它不管怎么表示和切片顺序没关系
# 切片的顺序和步长有关系，步长不写或者写正数，代表从左往右切
# 步长写为负数，代表从右往左切
# 从左往右切，起始位置在结束位置的右侧，那么切出来是空列表
# 从右往左切，起始位置在结束位置的左侧，那么切出来也是空列表


# 1-3查所有
# 遍历循环列表
# 直接遍历列表里面的所有元素
for item in list1:
    print(item)

# 根据列表的下标去遍历（列表的最大索引值 = 列表的长度 - 1）
for i in range(len(list1)):
    print(i,list1[i])


# 解构赋值
list_num = [1,2]
# a = list_num[0]
# b = list_num[1]

a,b = list_num #解构赋值 拆包赋值
print(a,b)


# 根据下标和元素一起来拿
# 里面牵扯两个点 1、enumerate作用把列表的下标和对应元素封装元组2、元组的拆包赋值（解构赋值）
for i,item in enumerate(list1):
    print(item)

















