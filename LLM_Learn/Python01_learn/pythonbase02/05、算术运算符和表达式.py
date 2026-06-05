num1 = 10
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(10 // 3)  #只拿结果的整数部分
print(num1 % num2)
print(num1 ** 3)


# 坑：
# 只要有除法参与的运算，除数不能为0，否则报错，异常错误叫除0异常
# print(10 / 0)
# print(10 % 0)
# print(10 // 0)


# 拿一个数字各个位上的数678
bai = 678 // 100
# shi = 678 % 100 // 10
shi = 678 // 10 % 10
ge = 678 % 10

print(bai,shi,ge)




