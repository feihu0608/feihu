# 字面量
dog = {
    "name":"旺财",
    "age":3,
    "color":"yellow",
    "z":1000
}

dog1 = {
    1:"旺财",
    2:3,
    6:"yellow",
    3:1000
}


# 成员判断(字典成员判断判断的是键而不是值)
print('name' in dog)
print(3 in dog)

# 统计(以键的大小来判断 字符串就是判断字符串的大小)
print(max(dog))
print(min(dog))
# sum(dog)



print(max(dog1))
print(min(dog1))
print(sum(dog1))

# 坑： 统计的时候 sum求和键必须是数字











