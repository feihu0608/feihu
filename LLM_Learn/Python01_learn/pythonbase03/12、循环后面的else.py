for i in range(1,11):
    if i % 3 == 0:
        break
    print(f"我爱你杨幂{i}")
else:
    print("我爱你赵丽颖")

# 循环正常结束，才会走else的代码块，break代表循环非正常结束，那么else代码块不走