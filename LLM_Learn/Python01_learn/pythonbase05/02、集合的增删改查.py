# 查： 无序代表没下标（无法单个查无法切片查）
# 遍历所有元素
set1 = {1,2,3,4,5}
for item in set1:
    print(item)



# 增：
# 单个增
# set.add(x)
# set.update(可迭代对象)
set1.add(6)
print(set1)

# 一下子增多个
set1.update([1,2,3,4,5,7,8,9])
print(set1)



# 删：
# remove(目标元素)：目标元素存在时删除元素，目标元素不存在时报错
# 不会返回删除的数据，返回的是None
# result = set1.remove(10) #删除不存在的炸
result = set1.remove(1)
print(result,set1)



# discard(目标元素)：目标元素存在时删除元素，目标元素不存在时安静的忽略
# 不会返回删除的数据，返回的是None
result = set1.discard(5)
# result = set1.discard(12) 删除不存在的不炸
print(result,set1)


# pop()：删除集合中的第一个元素并返回, 空集合报错
result = set1.pop()
print(result,set1)

set2 = set()
# set2.pop() # 空集合炸





# 改：先删除再添加
# 想把6改为66
set1.remove(6)
set1.add(66)
print(set1)


