# 所谓的动态规划 就是将重复的子问题 记录下来 复用 以减少重复计算 提高效率
# 时间复杂度 O(n)  空间复杂度O(1)
def climb(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a , b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


print(climb(6))



