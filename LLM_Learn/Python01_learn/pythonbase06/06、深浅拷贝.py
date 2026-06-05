import copy
a = 100
b = copy.copy(a)
print(a,b,id(a),id(b))
# 拷贝最终成功没成功要看有没有新的地址空间，虽然我们最终得到数据结果，但是拷贝不存在
# 拷贝存在了才能探讨深浅拷贝
# 不可变数据不存在拷贝



# 拷贝和深浅拷贝探讨的是可变数据
dict1 = {
    "name":"杨幂",
    "age":18,
    "movies":["仙剑","宫","三生三世"]
}
dict_new = copy.copy(dict1)
print(dict1,dict_new,id(dict1),id(dict_new))
print(id(dict1["movies"]),id(dict_new["movies"]))

# 深拷贝
# copy.deepcopy
dict_new = copy.deepcopy(dict1)
print(dict1,dict_new,id(dict1),id(dict_new))
print(id(dict1["movies"]),id(dict_new["movies"]))



# 后期我们要传递一个容器给函数，但是我又不想让函数内部对我这个可变容器有任何的影响
# 此时，我们就可以使用深浅拷贝来解决，至于是深还是浅，由你的业务决定


