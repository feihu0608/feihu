# 把整数转化为进制数展示
num = 13
print(bin(num)) #2
print(oct(num)) #8
print(hex(num)) #16

# 把一个字符串数字当2进制对待，去转化为整数
num = '11'
print(int(num, 2))


# repr(x) 把字符串会直接添加引号打印  转义字符会原样打印出来，转义效果看不到
str1 = "我爱你\n赵丽颖"
result = str(str1)
print(result)

result = repr(str1)
print(result)


# **eval(x)**  把一个字符串当中一条执行语句去执行
# 虽然可以执行语句，但是太灵活，慎用
str1 = "10 + 20"
print(str1)
result = eval(str1)
print(result)












