from collections.abc import Iterable

str1 = 'kasjdha1231234'
str2 = "asdkldjasdl;123"
str3 = """

    我爱你赵丽颖128947
    askldjkasdkl;
    asjkdasldadadd

""" #文档注释

print(str1)
print(str2)
print(str3)

str4 = str(123123)
print(str4)


# 原始字符串(后期我们学习正则表达式用的比较多)
str5 = r"asjkdhask\nldjad"
print(str5)

print(str5[1])
print(len(str5))
# str5[1] = "asdasd" #炸了后面的代码就不走了



# 字符串的查
print(str5[1])
print(str5[1:6])
for item in str5:
    print(item)

for i in range(len(str5)):
    print(i,str5[i])

for i,item in enumerate(str5):
    print(i,item)

# 其它操作
# 成员判断 in
print('zadsds' in str5)
print('kdhas' in str5)


# 重复 *
print("*" * 30)
# 拼接 +
print(str5 + "我爱你赵丽颖")
# 统计
# str.index()
print(str5.index(r'\n'))

# str.count()
print(str5.count('a'))

print(max(str5))
print(min(str5))

print(enumerate([1,2,4]))
for item in enumerate([1,2,4]):
    print(item)


# for item in enumerate({"name":"张三","age":18}):
#     print(item)

result = {"name":"张三","age":18}.keys()
print(result)

print(isinstance(result, Iterable))
# Iterable

