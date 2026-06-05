# 5、位置参数解包传参（实参）
# def fn(a,b):
#     print(a,b)

# 正常位置传参
# fn(1,2)



# 位置传参解包

#位置传参的时候解包的对象
# list1 = [10,20]
# tuple1 = (30,40)
#
# print("哈哈哈哈",*list1)
# fn(*list1) #  fn(10,20)
# fn(*tuple1)#  fn(30,40)




# 关键字参数解包传参
def fn1(a,b):
    print(a,b)
# 正常关键字传参
fn1(a=10,b=20)

# 关键字解包对象是字典
# 关键字形参的名字必须和字典的键要对应
dict1 = {"a":100,"b":200}
fn1(**dict1) #fn1(a=100,b=200)




# 位置传参和关键字传参解包混合

def fn2(a,b,c,d):
    print(a,b,c,d)

list2 = [10,20]
dict2 = {"c":100,"d":200}

fn2(10,20,c=30,d=40)
fn2(*list2,**dict2)





# 6、强制使用位置参数或者关键字参数
# 强制使用位置参数或关键字参数： / 前的参数必须使用位置传参，*后的参数必须用关键字传参。
# 一般我们不去规定，但是后期我们在看框架源码的时候，源码当中会出现
def print_info(name, age, /, gender, hobby, *,  city):
    print(f"{name} 的年龄是：{age}，性别是：{gender}，爱好是：{hobby}，城市是：{city}")

# print_info(name="yangmi",age=10,gender="女",hobby=["足球"],city="深圳")

print_info("杨幂",18,"女",["足球"],city="深圳")
