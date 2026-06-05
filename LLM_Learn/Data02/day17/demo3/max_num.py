def maximumSwap(num):
    # 初始化最终结果为原始数字
    result = num
    # 将数字转换为字符列表，方便交换每一位数字
    num_list = list(str(num))
    # 记录从后往前遍历时，当前最大数字的索引，初始值为-1
    max_index = -1

    # 从后往前遍历每一位数字（从最后一位到第一位）
    for i in range(len(num_list) - 1, -1, -1):
        # 如果当前位数字 > 已记录的最大数字
        # 更新最大值的索引为当前索引
        if num_list[i] > num_list[max_index]:
            max_index = i

        # 如果当前位数字 < 已记录的最大数字
        # 说明交换后能让数字变大，执行交换尝试
        else:
            # 交换当前位和最大值位
            num_list[i], num_list[max_index] = num_list[max_index], num_list[i]
            # 把交换后的数字转成整数，和当前最大结果比较，保留更大值
            result = max(result, int("".join(num_list)))
            # 回溯：交换回去，恢复原数组，继续遍历下一位
            num_list[i], num_list[max_index] = num_list[max_index], num_list[i]

    # 遍历结束，返回能得到的最大数字
    return result

if __name__ == "__main__":
    print(maximumSwap(2736))
