"""
    冒泡排序优化
"""

def bubble_sort_optimize(nums):
    n = len(nums)

    for i in range(n - 1):

        swapped = True  # 标记 初始化为True

        for j in range(n - 1 - i):

            if nums[j] > nums[j + 1]:
                swapped = False  # 将标记设置为False
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(f"第{i + 1}轮比较后元素的顺序", nums)
        if swapped:
            break


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 10, 5, 6, 7]
    bubble_sort_optimize(list1)
    print(list1)
