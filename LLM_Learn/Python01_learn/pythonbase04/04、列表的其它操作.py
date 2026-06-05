# 1列表排序
list1 = [3,1,2,4,5]
# result = list1.sort(reverse=True) #在原列表身上直接排序
# print(result,list1)
# list.sort(reverse=True) 在原列表身上排序 reverse=True决定是升序还是降序


# 不会在原列表身上进行排序，而是生成新的列表进行排序 reverse=True决定是升序还是降序
# result = sorted(list1,reverse=True)
# print(result,list1)


# 2列表反转
result = list1.reverse() #反转列表，在原列表身上直接反转
print(result,list1)



# 3列表重复
list2 = [1,2,3]
print(list2 * 3)
# 列表拼接
list3 = ['yangmi','zhaoliying']
print(list2 + list3)
print(list2,list3)

# 成员判断
print(1 not in list2)



# 列表统计
score_list = [88,90,100,99,56,99]
print(sum(score_list))  #元素必须是数字才能干活
print(max(score_list)) #最大值
print(min(score_list)) #最小值

# 获取指定的元素第一次出现的下标，从左往右去找，可以指定起始的位置
result = score_list.index(99,4)  #求列表当中某个元素的下标 第一次出现的
print(result)

# 用来统计元素在列表当中出现的次数
result = score_list.count(99)
print(result)

# 压缩 不光可以对列表操作，只要是可迭代对象都可以操作
list4 = [1,2,3]
list5 = ('赵丽颖','杨幂','迪丽热巴')
# 压缩
result = zip(list4,list5) #是一个压缩后的可迭代对象
print(result)
for i,item in result:
    print(i,item)


# 解压缩
zip_list = [(1,"哈哈"),(2,"呵呵"),(3,"嘻嘻")]
result = zip(*zip_list)
print(result)
for item in result:
    print(item)
































