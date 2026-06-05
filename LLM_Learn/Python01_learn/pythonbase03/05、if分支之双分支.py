# 给定天气，天气好就出去玩，不好在家写作业
# 随机获取一个1到100的整数，偶数就爱赵丽颖，奇数就爱杨幂


# weather = True
# if weather:
#     print("我们出去happy")
# else:
#     print("在家写作业")
#
# print("我爱你杨幂")



import random
rand_num = random.randint(1,68)
print(rand_num)

if rand_num % 2 == 0:
    # 偶数
    print("我爱你杨幂")
else:
    # 奇数
    print("我爱你赵丽颖")

print("我爱你刘诗诗")