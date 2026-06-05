"""
    复杂度
    第一种：使用耗时来表示 但是这种表示在不同的设备会有差异 所以不可取
    第二种：T表示法 用于精确表示当前算法一共执行了多少步骤   T(n) = 5n + 5
    第三种：O表示法 只看增长趋势 忽略常数 忽略系数 忽略低阶 O(n)

    T(n) = 2n + 3   
    T(n) = 3n² + 4  O(n²)
    T(n) = 7n³ + 4n²  O(n3)



"""
import time


def get_sum(nums):
    result = 0 #最终的结果   1次赋值操作
    i = -1  # 初始遍历下标为-1   1次赋值操作
    while(i := i + 1) < len(nums):  # n + 1次加法计算 、 n + 1次赋值、 n + 1比较
        result += nums[i]  # n 次加法计算  n次赋值操作
    return result


if __name__ == '__main__':
    start = time.time()
    get_sum = get_sum([1,2,3,4,5,6])
    end = time.time()
    print(end - start)