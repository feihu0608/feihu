# 一、增：
list1 = [1,2,3,4,3,5]
# print(list1[6])  #下标越界异常报错  炸

# 1、list.append(x)
# 在原数组的末尾追加一个元素
# list1.append(100)
# print(list1)
# list1.append([6,7,8]) #如果元素又是一个列表，那么最终就是嵌套列表
# print(list1)

# 2、list1.extend(list2)
# 让我们可以一次性添加多个元素，只是需要用可迭代对象去做，传递一个列表最终不是嵌套列表
# 把列表里面的元素添加到原列表当中
# list1.extend('yangmi')
# list1.extend([6,7,8,9])
# print(list1)


# 3、list.insert(index, x)
# list1.insert(2,200)
# list1.insert(2,[100,200])  #形成嵌套列表
# print(list1)

#
# 二、改：

# list[index] = X
# 单个改
# list1[2] = 33
# print(list1)
#
# # list1[start:end] = list2
# # 多个改
# list1[3:] = [44,55]
# print(list1)



# 三、删：
# 1、del list[index]
# del list1[1]
# print(list1)
# del list1[7] #越界 炸
# print(list1)

# del list1[2:4]  #根据切片删多个
# print(list1)


# 2、list.remove(x)  #删除第一个出现的元素
# result = list1.remove(3)
# print(list1,result)



# 3、list.pop([index])
# result = list1.pop()  #如果不指定下标，默认删最后一个元素，并且把删除的元素返回
# print(result,list1)

# result = list1.pop(4)  #根据指定的下标去删除，返回删除的元素
# print(result,list1)




# 4、list.clear()
list1.clear()
print(list1)