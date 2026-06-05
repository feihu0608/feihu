"""
    快速排序  双向指针对撞版本

    1.选取最左边的元素为基准 pivot
    2.左指针向右找 大于基准的数
    3.右指针向左找 小于等于基准的数
    4.两指针为不重合的时候 交换元素 继续收缩区间
    5.两指针重合 该下标即为基准该存放的位置
    6.基准确认以后 递归排序左右区间(重复以上操作)

"""

def quick_sort(arr,left,right):
    # 如果left大于等于right 说明只剩下一个元素
    if left >= right:
        return

    # 选取最左边的元素为基准值
    pivot = arr[left]

    # 不能直接使用left和right 因为有可能涉及到移动位置
    l = left
    r = right

    while l < r:
        # 这个循环是右指针向左找，找到 <= pivot 的元素停下
        while l < r and  arr[r] > pivot:
            r -= 1
        # 这个循环是左指针向右找，找到 > pivot 的元素停下
        while l < r and arr[l] <= pivot:
            l += 1

        if l < r:
            # 交换左指针和右指针元素的位置
            arr[l], arr[r] = arr[r], arr[l]

    # 代码能执行到这里 说明 左右重合了
    # 将基准值 和 重合的位置交换
    arr[left] , arr[l] = arr[l] , arr[left]
    # 新的一轮开始 处理左半部分 左边的指针不变 右边指针等于重合位置-1
    quick_sort(arr,left,l - 1)
    # 新的一轮开始 处理右半部分 右边的指针不变 左边指针等于重合位置+1
    quick_sort(arr,l + 1, right)


if __name__ == '__main__':
    nums = [1,5,3,4,2]
    quick_sort(nums,0,len(nums)-1)
    print(nums)