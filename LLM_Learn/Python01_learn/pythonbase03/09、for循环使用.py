# for i in range(100):
#     print(f"我爱你{i}")
#
# print("我爱你杨幂")


# for i in range(101,1,-1):
#     print(i)


# 案例
#1、 获取1到100的数
# for i in range(1,101):
#     print(i)

#2、 获取1到100的偶数
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)

#3、 求1到100的和
# 累加器思想 定义一个变量代表和 一开始这个值是0，然后没拿到一个数，就累加到这个和身上
# 循环完成，这个和的变量里面的值就是我们要的结果
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)


#4、 求10的阶乘
# 类似求和 累乘
# mul = 1
# for i in range(1,11):
#     mul *= i
# print(mul)


#5、 求1到10的阶乘和
# sum = 0
# mul = 1
# for i in range(1,11):
#     mul *= i
#     sum += mul
# print(sum)


#6、 求100到999能被3整除或者位上有3的数
# for i in range(100,1000):
#     bai = i // 100
#     shi = i // 10 % 10
#     ge = i % 10
#
#     if bai == 3 or shi == 3 or ge == 3 or i % 3 == 0:
#         print(i)


#7、 求100到999的水仙花数(每个位上的数字立方之和等于这个数本身，那么这个数就是水仙花数)
for i in range(100,1000):
    bai = i // 100
    shi = i // 10 % 10
    ge = i % 10
    if bai ** 3 + shi **3 + ge ** 3 == i:
        print(i)



#8、 进度条模拟
import time
for i in range(1,101):
    print("=",end='')
    time.sleep(0.5)




