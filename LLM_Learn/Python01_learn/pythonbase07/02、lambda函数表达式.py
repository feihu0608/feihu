def add(a, b):
    return a + b

#
# print(add(10, 20))


# add = lambda a, b: a + b
# print(add(1, 2))

# 1、lambda在函数内部调用,不管什么函数都可以当参数传递给另外一个函数
def fn(a,b,func):
    return func(a,b)

print(fn(1, 2, add))

# 2、lambda可以作为参数传递给一些内置函数

# sorted ********
star_list = [
    {"id":1,"name":"杨幂","age":38},
    {"id":2,"name":"赵丽颖","age":39},
    {"id":3,"name":"刘诗诗","age":40},
    {"id":4,"name":"迪丽热巴","age":28},
    {"id":5,"name":"柳岩","age":48},
]

# 我想让你把这个列表当中的所有明星排序***************  面试题
# 执行流程：遍历传递的列表，拿到列表当中每个元素，传递给lambda的参数，执行函数返回的值，作为排序的key
new_list = sorted(star_list,key=lambda x:x['age'],reverse=True)
print(new_list)


# star_list.sort(key=lambda x:x['age'],reverse=True)
# print(star_list)


# filter 是返回我们指定的lambda函数返回值为true的元素  （推导式可以直接解决所以后期用的不多）
list1 = [1,2,3,4,5]
# list2 = [item for item in list1 if item > 3]

result = filter(lambda x:x > 3,list1)  #返回的不是list而是一个可迭代对象
result1 = filter(lambda x:x['id'] < 3,star_list)  #返回的不是list而是一个可迭代对象
print(list(result1))




# map 映射 让你根据老的列表映射一个新的  新的列表当中每个数据都是和老的列表数据有关联，推导式可以直接解决
result2 = map(lambda x:x**3,list1)
print(list(result2))

# 3、作为标准库中函数的参数（参考详细文档，了解）
# 4、作为函数返回值（参考详细文档，了解）



# 注解的了解(需要注意)
# 普通的自定义函数：
def print_info_normal(name: str, species: str, age: (1,99) = 1) -> None:
    print(f"{name} 的品种是：{species}，年龄是：{age}")

# 调用函数
print_info_normal("旺财", "泰迪", 5)
print(print_info_normal.__annotations__) #用来保存注解的字典


# 什么是注解，本质就是注释说明









