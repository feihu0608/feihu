# > < >= <= == !=
# 比较运算主要就是做判断用的，最终只要是比较运算形成的表达式，最终表达式的值一定是布尔值

a = 100
b = 100
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)




# 坑
# 两个字符串比较操作
# 字符串比较方式：两个字符串从头开始依次比较字符的unicode码值，一旦比较有大小的结果，直接结束
# 如果比较的都是相等的，最终两个字符串才相等
str1 = "efabc"
str2 = "efabcd"
print(str1 > str2)











