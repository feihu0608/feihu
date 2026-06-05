#一、 列表的创建
# 字面量
list1 = [1,2,"yangmi",4,5] #正常列表
list2 = []  #空列表

# 函数创建
list3 = list(range(10))
list4 = list('asjkdhas')
print(list1)
print(list2)
print(list3)
print(list4,type(list4))

# 嵌套列表（多维列表）
list5 = [1,2,3,[4,5],6,7,['zhaoliying','yangmi']]

# 列表都有长度
print(list5,len(list5))
# 列表都有索引下标，可以让我们获取固定下标的值（下标都是0开始）
print(list5[4])
print(list5[6][1])














