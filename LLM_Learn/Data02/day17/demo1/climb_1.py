# f(5) = f(4) + f(3)
# f(4) = f(3) + f(2)
# f(3) = f(2) + f(1)
# f(2) = f(1) + f(0)
# O(2 ** n)
def climb(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 状态转移方程：f(n) = f(n-1) + f(n-2)
    return climb(n - 1) + climb(n - 2)


print(climb(10))