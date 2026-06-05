

"""
    归并排序
"""

# 拆分
def split(arr):
    # 拆分为单个单个的元素 那么就可以结束递归
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 # 找到中间下标
    left = split(arr[:mid]) # 切片左半部分 继续拆分
    right = split(arr[mid:]) # 切片右半部分 继续拆分

    # 合并操作
    return merge(left, right)


# 合并
def merge(left, right):

    result = [] # 准备一个空列表 用于存放排序之后的数据

    # 定义两变量都从0开始 因为我们最终要遍历两个有序数组 下标都从0开始
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 因为有可能 两个数组元素  一边少 一边多
    # 我们上方的循环是统一遍历的 所以最多遍历完长度最短的数组
    # 那么长度较长的数组 可定会有遗漏的一个元素 所以 追加在列表的末尾
    result += left[i:]
    result += right[j:]
    return result

if __name__ == '__main__':

    nums = [1,5,3,4,2]
    new_nums = split(nums)
    print(new_nums)


