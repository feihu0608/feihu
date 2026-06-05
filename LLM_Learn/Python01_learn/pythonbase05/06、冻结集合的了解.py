# 冻结集合其实本质就是不可变的集合
frozenset1 = frozenset([1,2,3])
print(frozenset1)
print(type(frozenset1))
# 冻结集合可以查不能改
for item in frozenset1:
    print(item)

# 冻结集合的作用后期就是用来作为字典的键
# 不可变就可以
# 一般后期我们不知道字典里面都有哪些键，为了防止键的冲突重复发生覆盖的问题，我们可以用一个冻结集合作为键
# 冻结集合一般字典里面是不存在这种键的
dict1 = {
    frozenset1:1
}
print(dict1)












