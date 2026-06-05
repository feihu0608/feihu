f = 1.456
# type是打印数据的类型
print(f,type(f))

num= 100
print(num,type(num))

# 复数
c = complex(5,4)
print(c,type(c))

# 小数和复数 都在这里归到浮点



# 坑
num1 = 0.1
num2 = 0.2
print(num1 + num2)


# 包就是我们所说的工具库，python自带了很多的工具库
import decimal
num1 = decimal.Decimal("0.1")
num2 = decimal.Decimal("0.2")
print(num1 + num2)








