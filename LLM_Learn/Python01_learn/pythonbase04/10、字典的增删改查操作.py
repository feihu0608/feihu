dog = {
    "name":"旺财",
    "age":3,
    "color":"yellow",
}

# 1查
# 1-1根据键去查值
print(dog["color"],dog["age"])
result = dog.get("name")
print(result)

# 1-2查所有
# 查所有的键（默认和列表元素遍历一样，遍历字典拿的就是键）
for item in dog:
    print(item)

# print(dog.keys())
for key in dog.keys():
    print(key)

# 查所有的值(一般不用)
for value in dog.values():
    print(value)

# 查所有的键和值
for key,value in dog.items():
    print(f"{key}的值是{value}")


# 增和改（操作的时候有则更改，无则添加）
# 单个
dog["haha"] = "呵呵"
dog["name"] = "大黄"
print(dog)


# 多个 有则更改，无则添加
dog.update({
    "age":1,
    "heihei":"嘻嘻"
})
print(dog)



# 删

# del dict[key]     根据键删除键值对，不存在报错
del dog["heihei"]
print(dog)
# del dog["aaaa"] #键必须存在，不存在报错



# dict.pop(key[,default])   根据键删除键值对并把这个键的值返回，如果键不存在报错，如果不想报错，可以设置默认值
result = dog.pop("age")
print(result,dog)

result = dog.pop("bbb",10)
print(result,dog)

# dict.popitem()    删除最后一个插入的键值对 返回键值组成的元组  空字典报错
result = dog.popitem()
print(result,dog)


# dict.clear()     清空字典
dog.clear()
print(dog)








