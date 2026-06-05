"""
    选择排序
"""


def selection_sort(nums):
    n = len(nums) #获取长度 循环中使用
    for a in range(n - 1) :   # 元素A的范围
        index = a # 将a的值 赋值给index 每一轮比较开始 index都等于a
        for b in range(a + 1,n):  # 元素B的范围
            # 如果条件成立 不交换位置 交换比较的元素a
            if nums[index] < nums[b]:
                index = b  # 将b的下标赋值给index
        if index != a:
            nums[index], nums[a] = nums[a], nums[index]

if __name__ == '__main__':
    list1 = [0,2, 1, 5, 4, 7, 3, 2, 10]
    selection_sort(list1)
    print(list1)
