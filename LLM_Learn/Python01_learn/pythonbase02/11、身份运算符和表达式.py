# is就是来看比较的两个人地址值是不是一样
# == 比较值的大小，值的大小相等就为True
a = 100
b = '100'
print(a is b,id(a),id(b))   #False 整数和字符串id地址不一样
print(a is int(b),id(a),id(int(b))) #True 整数100和100都是小整数池当中的1，地址值一样
print(a is not float(b),id(a),id(float(b))) #False 整数100和浮点数100.0地址值不一样

print(a == b) # False 一个整数和一个字符串不可能相等
print(a == int(b)) #True 100 和强转出来的100大小一样
print(a == float(b)) #True 100和强转出来的100.0大小也一样



a = 10
print(a)











