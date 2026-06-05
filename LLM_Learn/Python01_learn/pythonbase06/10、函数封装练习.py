# 封装函数实现打印100次我爱你
# def print_love():
#     for i in range(100):
#         print("我爱你")
#
# print_love()




# 封装函数实现打印n遍我爱你
def print_love(n):
    for i in range(n):
        print("我爱你")

print_love(10)


# 封装函数实现打印n行n列的直角三角形
def print_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print("*",end="")
        print("")


print_triangle(10)
print_triangle(5)



# 封装函数实现一个整数列表中所有奇数的和

def sum_odd(a):
    return sum([i for i in a if i % 2 ==1])

list1 = [1,2,3,4,5,6,7,8,9,10]
print(sum_odd(list1))


# 封装函数实现判断一个数是不是质数
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True


print(is_prime(4))

# 求1到100之间的所有质数组成列表
list2 = [i for i in range(1,101) if is_prime(i)]
print(list2)





# 封装函数实现返回一个格式化的日期时间
# import datetime
# datetime.datetime.now()


# from datetime import datetime
# print(datetime.now())


def format_date_time():
    from datetime import datetime
    current_date_time = datetime.now()
    # year = str(current_date_time.year)
    # month = str(current_date_time.month)
    # day = str(current_date_time.day)
    # hour = str(current_date_time.hour)
    # minute = str(current_date_time.minute)
    # second = str(current_date_time.second)
    # str1 = year + "年" + month + "月" + day + "日" + "  " + hour + "时" + minute + "分" + second + "秒"
    return current_date_time.strftime("%Y年%m月%d日 %H时%M分%S秒")


print(format_date_time())










