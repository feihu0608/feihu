def permute(nums):
    # 存储最终的所有排列结果
    result = []

    # 定义回溯函数，start表示当前正在确定第start个位置的元素
    def backtrack(start):
        # 递归终止条件：start等于数组长度，说明所有位置都已确定
        # 此时nums就是一个完整排列，将其拷贝加入结果集
        if start == len(nums):
            result.append(nums[:])  # nums[:]是浅拷贝，避免后续修改影响已保存的结果
            return
        # 遍历从start开始的所有元素，尝试将每个元素放到start位置
        for i in range(start, len(nums)):
            # 交换：把第i个元素放到当前start位置（做选择）
            # 避免自己和自己交换，减少无效操作
            if start != i:
                nums[start], nums[i] = nums[i], nums[start]
            # 递归：固定好start位置，继续处理下一个位置 start+1
            backtrack(start + 1)
            # 回溯：撤销交换，恢复数组原状，回到上一步状态（撤销选择）
            # 保证下一轮循环时数组是原始状态，不影响其他分支
            if start != i:
                nums[start], nums[i] = nums[i], nums[start]
    # 从第0个位置开始生成全排列
    backtrack(0)
    # 返回所有排列结果
    return result

if __name__ == '__main__':
    print(permute([1,2,3]))