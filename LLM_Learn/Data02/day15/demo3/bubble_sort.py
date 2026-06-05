

"""
    冒泡排序实现
    外层循环控制轮数 n - 1
    内层循环控制每一轮的次数 n - 1 - i
"""

def bubble_sort(nums):
    n = len(nums)

    for i in range(n - 1): # 控制轮数

        for j in range(n - 1 - i): # 控制次数

            if nums[j] <  nums[j + 1]: # 条件成立

                nums[j], nums[j + 1] = nums[j + 1], nums[j] # 交换位置
        print(f"比较第{i + 1}轮元素的顺序：" , nums)

if __name__ == '__main__':
    list1 = [2, 1, 5, 4, 7, 3, 2, 10]
    bubble_sort(list1)
    print(list1)