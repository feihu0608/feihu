# - 两个布尔类型数据进行算术运算时自动升级为int
bol1 = True
bol2 = True
print(bol1 + bol2)

# - 两个int类型数据进行除法/运算时自动升级为float
num1 = 10
num2 = 2
result = num1 / num2
print(result,type(result))


# - 两个不同数值类型数据进行混合运算，小的类型自动升级为大的类型 bool<int<float<complex
bol3 = True
num3 = 100
fnum = 3.56
print(bol3 + num3)
print(bol3 + fnum)
print(num3 + fnum)





