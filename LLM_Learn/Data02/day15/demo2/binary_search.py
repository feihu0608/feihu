"""
    二分查找算法
    要求：序列必须是有序 否则不能保证准确性  如果找到 则返回对应元素的下标
    如果未找到 则返回负值 通常是 -1
"""

def binary_search(nums:list[int],target:int)->int:
    if not nums or len(nums)==0:
        return -1
    begin = 0  # 起始位置
    end = len(nums) - 1  # 结束位置
    while begin <= end:
        mid = begin + (end - begin) // 2  #  begin + (end - begin ) // 2  推荐写法 避免造成内存溢出
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            # 从左边找
            end = mid - 1
        else:
            begin = mid + 1

        # mid = (begin + end) // 2
    return -1

if __name__ == "__main__":
    list1 = [1,2,3,4,5,6,7,8,9,10]

    index = binary_search(list1,7)

    print(index)




