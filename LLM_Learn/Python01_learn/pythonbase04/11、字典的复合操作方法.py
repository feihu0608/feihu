# dict1 = {
#     "name":"杨幂",
#     "age":18
# }
#
# name = dict1.setdefault("name")
# haha = dict1.setdefault("haha",10)
# print(haha,dict1)


# 把指定的参数序列，作为key添加键值对,会生成一个新的字典，原字典不变
# 几乎不用
dict2 = {}
result = dict2.fromkeys("dgha",10)
print(dict2,result)
