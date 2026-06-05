def max_sub_arr(nums):
    # 创建和原数组长度一致的新数组 用于保存累计和
    # 不一定是最大值
    dp = [0] * len(nums)

    # 第一个元素 只能自己构成子数组
    dp[0] = nums[0]

    # 默认第一个是最大值
    max_num = nums[0]


    for i in range(1, len(nums)):
        # 选择前边子数组 dp[i - 1] + nums[i]
        # 不选择 则从当前nums[i]重新开始
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

        max_num = max(max_num,dp[i])

    return max_num
print(max_sub_arr([1,2,3,4]))