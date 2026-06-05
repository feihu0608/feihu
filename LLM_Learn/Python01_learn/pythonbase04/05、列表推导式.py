# list1 = []
# for i in range(1,11):
#     list1.append(i)
# print(list1)

# 列表推导式的写法   拿1到10
list1 = [i for i in range(1,11)]
print(list1)


# 现在要拿1-10的偶数
# list1 = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)
# if相当于是for循环里面写的代码
list2 = [ i for i in range(1,11) if i % 2 == 0]
print(list2)




list3 = [1,2,3]
list4 = ['yangmi','zhaoliying','dilireba']
# result_list = []
# for item1 in list3:
#     for item2 in list4:
#         result_list.append((item1,item2))
# print(result_list)
result_list = [(item1,item2) for item1 in list3 for item2 in list4]
print(result_list)






