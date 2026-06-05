
"""
    插入排序
    左边第一个元素天然有序
    后续右边的元素 依次与左边有序区域的元素进行比较 找到合适的位置 进行插入
"""


def insertion_sort(nums):

    n = len(nums)

    for i in range(1, n):

        temp = nums[i] # 记录当前每轮开始 i位置的元素值

        # 从i - 1 向前遍历  扫描
        j = i - 1

        # 因为是从右往左遍历  所以j必须大于等于0
        # 因为是升序 所以 nums[j] > temp
        while j >= 0 and nums[j] > temp:
            # 将左边的元素  直接覆盖右边的位置
            nums[j + 1] = nums[j]

            j -= 1  # 依次减少j的取值 表示往左边进行比较

        # 循环执行完毕 说明有序区全部遍历完成
        nums[j + 1] = temp


if __name__ == '__main__':
    list1 = [2, 1, 5, 4, 7, 3, 2, 10]

    insertion_sort(list1)

    print(list1)


