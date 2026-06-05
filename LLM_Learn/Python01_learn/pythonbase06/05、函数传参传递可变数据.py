# 形参变量 = 老的数据（数据相同） 那么形参变量里面的地址和实参变量里面的地址不一样

def fn(a):
    print(a,id(a))
    a = [1,2,3]
    print(a,id(a))

a = [1,2,3]
fn(a)
print(a,id(a))


# 形参变量 = 新的数据   那么形参变量内部地址发生改变  不会影响外部实参数据变量地址

def fn2(a):
    print(a,id(a))
    a = [1,2,3,4]
    print(a,id(a))

a = [1,2,3]
fn2(a)
print(a,id(a))



# 可变数据可以操作容器内部的数据，
# 形参拿到实参数据的地址并不变，而是修改容器里面的数据，此时内外数据都会修改，因为地址没变
def fn3(a):
    print(a,id(a))
    # a = [1,2,3]  操作整体变量的地址
    a[2] = 33
    print(a,id(a))


a = [1,2,3]
fn3(a)
print(a,id(a))


# 这个是在原列表上进行操作
list1 = [1,2,3]
print(list1,id(list1))
list1 *= 2
print(list1,id(list1))


# 先弄新的列表操作完了把新列表地址赋值
list2 = [1,2,3]
print(list2,id(list2))
list2 = list2 * 2
print(list2,id(list2))















