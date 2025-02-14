def twoSum(nums, target):
    # 创建一个空的哈希表，用于存储元素及其索引
    num_dict = {}
    # 遍历数组中的每个元素及其索引
    for i, num in enumerate(nums):
        # 计算目标值与当前元素的差值
        complement = target - num
        # 检查差值是否已经存在于哈希表中
        if complement in num_dict:
            # 如果存在，返回差值的索引和当前元素的索引
            return [num_dict[complement], i]
        # 将当前元素及其索引存入哈希表中
        num_dict[num] = i
    # 如果没有找到符合条件的两个数，返回空列表
    return []

# 测试示例
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # 输出: [0, 1]