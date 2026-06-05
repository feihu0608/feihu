flag = True
print(flag,type(flag))
flag = False
print(flag,type(flag))

# 布尔值bool是一个类型，这个类型当中只有两个值True和False
# 其实本质bool值，在存储的时候，存储的也是数字 True是1  False是0
# bool其实是int的子类型
print(isinstance(flag, bool))
print(isinstance(flag, int))# bool其实是int的子类型
print(isinstance(flag, str))






