"""
List
"""

# 创建列表
numbers = [1, 2, 3, 4, 5]
# 使用切片操作获取子列表
subset = numbers[1:3]
print(subset)  # [2, 3]
# -1表示最后一个元素
subset = numbers[1:-1]
print(subset)  # [2, 3, 4]
