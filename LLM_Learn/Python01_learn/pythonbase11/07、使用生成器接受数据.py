# 使用send发送数据给生成器，修改步长


def numgenderator(n):
    num = 1
    step = 1
    while num <= n:
        value = yield num
        print(value)
        if value:
            step = value
        num += step

num_generator = numgenderator(100)
# next(num_generator) #==> num_generator.send(None)
print(num_generator.send(None))  #第一次没有发送值，目的是为了启动生成器的函数执行
print(num_generator.send(None))
print(num_generator.send(None))
print(num_generator.send(None))
print(num_generator.send(None))


# 我要改变步长
print(num_generator.send(2))

print(num_generator.send(None))
print(num_generator.send(None))
print(num_generator.send(None))

# 我要改步长

print(num_generator.send(1))







