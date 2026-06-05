#打印100次赵丽颖
def print_love(n,name):
    for i in range(n):
        print(f"我爱你{name}")
    return 10000

result = print_love(10,'yangmi')
print(result)


def add(a,b):
    result = a + b
    return result,"哈哈"

result = add(10,20)
print(result)



def get_max_value(list1):
    return max(list1)

print(get_max_value([29,18,90,45]))


def return_test():
    a = 100
    print(a)
    return  #立即结束函数调用
    b = 200
    print(b)

return_test()

