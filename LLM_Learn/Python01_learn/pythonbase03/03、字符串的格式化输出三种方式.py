name = "yangmi"
age = 18
height = 1.789
# 1、占位符 格式化输出（在python2的时候用的比较多）
# 通过.2f % 可以控制小数的位数，默认不写是6位，控制小数点的时候是四舍五入的
print("我的名字叫%s,年龄是%d，身高是%.2f" %(name,age,height))

# 2、 format方法去格式化（python2和python3中间过渡）
# 2-1: 按照位置进行填充  如果要对小数保留，那么在花括号当中 :.xf,也是四舍五入
print("我的名字叫{},年龄是{}，身高是{:.2f}".format(name,age,height))

# 2-2：按照参数下标索引去填充
print("我的名字叫{1},年龄是{2:.2f}，身高是{0}".format(name,age,height))

# 2-3：按照名称关键字去填充
print("我的名字叫{a},年龄是{b}，身高是{c:.2f}".format(b=age,c=height,a=name))


# 3、 f-string方式去格式化(python3推荐使用)
print(f"我的名字叫{name},年龄是{age}，身高是{height:.2f}")
# 坑：{{}} 相当于是转义 相当于只写了一个{} 而且里面的变量会当做字符串原样打印
print(f"我的名字叫{{name}},年龄是{age}，身高是{height:.2f}")
















