# 字面量
t1 = (1,2,3)
t2 = ()
print(t1,type(t1),t2,type(t2))
# t1[0] = 11 #元组不可变

# 函数
t3 = tuple([1,2,3])
print(t3,type(t3))

# 坑：如果元组当中只有一个元素,元素后面一定要带一个逗号
t4 = (6,)
print(t4,type(t4))

# 嵌套元组
t5 = ((1,2,3),4,5,(6,7))
print(t5,type(t5))


print(t5[2]) #5
print(t5[3][0]) #6
print(len(t5))








