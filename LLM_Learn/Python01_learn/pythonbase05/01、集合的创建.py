# 字面量
set1 = {1,2,3,4,3,4}
print(set1)

set2 = {} # 空集合没办法使用字面量 这样写是一个空字典
print(set2,type(set2))

# 函数
set3 = set("adhaskld")
print(set3)

set4 = set((1,2,3,4,3,4))
print(set4)

# 空集合只能用函数创建
set5 = set()
print(set5,type(set5))

print(len(set5)) #求长度
print(len(set4)) #求长度







