a = 100
b = True
print(a,type(a))
print(b,type(b))

print(isinstance(a,int))
print(isinstance(a,bool))


print(isinstance(b,int))
print(isinstance(b,bool))

# type主要就是看这个数据的主类型
# isinstance 主要用于判断这个数据是不是这个家族（主类型或者这个主类型的父类型）