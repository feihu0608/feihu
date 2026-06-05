# 强制类型转化主要是通过内置的几个函数进行的
# int()
# float()
# bool()
# str()

#1、 把其他类型强转为整数类型
# fnum = 1.567
# result = int(fnum)
# print(result,type(result)) #小数转整数是截断操作，只拿整数部分
#
# bol = False
# result = int(bol)
# print(result,type(result)) #True为1 False为0
#
# # str1 = "askudhasldkjakl"  #炸 报错
# # str1 = "askdua15askldja"  #炸 报错
# # str1 = "10asdghasdkj"  #炸 报错
# str1 = "10"  #完美转化
# # str1 = "10.345" #炸 报错
# # str1 = ""  #炸 报错
# result = int(str1)
# print(result,type(result))  #字符串转整数必须看起来是一个整数，其余报错
#
#
# non = None
# result = int(non)
# print(result,type(result)) # None转化整数报错



#2、 把其他类型强转为小数类型
# num = 100
# result = float(num)
# print(result,type(result)) #完美转化 后面添加小数点0
#
# bol = False
# result = float(bol)
# print(result,type(result)) #完美转化
#
# # str1 = "asdhaskldjaskldj" #炸
# # str1 = "10asdhaskldjaskldj" #炸
# # str1 = "asdha10skldjaskldj" #炸
# # str1 = "-10"  #完美转化
# # str1 = "10.89"  #完美转化
# # str1 = "10.89.23"  #炸
# # str1 = "" #炸
# # str1 = "True" #炸
# # str1 = " " #炸
# # result = float(str1)
# # print(result,type(result)) #看起来是一个数字就可以转化，否则炸
#
#
# non = None
# result = float(non)
# print(result,type(result))  #炸


#3、 把其他类型强转为布尔
# 整数和小数转化布尔值非0即为真
# num = -0.1
# result = bool(num)
# print(result,type(result))  #非0即为真


# str1 = "ashaskdjaskdlj"
# str1 = "ashaskd123jaskdlj"
# str1 = "123ashaskd123jaskdlj"
# str1 = "123"
# str1 = "123.123"
# str1 = "0"
# str1 = " "
# str1 = ""
# result = bool(str1)
# print(result,type(result)) #非空串即为真


# non = None
# result = bool(non)
# print(result,type(result)) #None转布尔是False



#4、 把其他类型强转为字符串
num = 100
num = 0
num = 1.23
num = 0.0
result = str(num)
print(result,type(result))

bol = False
result = str(bol)
print(result,type(result))


non = None
result = str(non)
print(result,type(result))

# 所有数据转字符串都完美转化 直接加引号












