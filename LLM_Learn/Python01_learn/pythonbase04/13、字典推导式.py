# 语法糖  简写  循环
# dict1 = {}
# for i in range(1,11):
#     dict1[i] = i**2
# print(dict1)

dict1 = {i:i**2 for i in range(1,11)}
print(dict1)


dog = {
    "name":"旺财",
    "age":3,
    "color":"yellow",
    "z":1000
}

# dict2 = {}
# for k,v in dog.items():
#     dict2[k] = v
# print(dict2)

dict2 = {k:v for k,v in dog.items()}
print(dict2)


