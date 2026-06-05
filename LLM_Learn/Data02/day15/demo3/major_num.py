# 可读性 大于 极致简洁

def major_num(nums):
    count = 0  # 计数器用于记录总票数
    candidate = None  # 候选人
    # 遍历序列
    for num in nums:
        # 如果清零 当前的数值为候选人
        if count == 0:
            candidate = num
        # 如果遇到相同的元素 则计数器+1
        if num == candidate:
            count += 1
        else:  # 否则 - 1
            count -= 1
    return candidate


if __name__ == '__main__':
    list1 = [1, 1, 2, 2, 2, 2]
    print(major_num(list1))
