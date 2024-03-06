"""
reduce() 用于对参数序列中的元素进行累积。
"""
from functools import reduce

lt = [1, 2, 3, 4, 5]

# 计算列表元素之和
res = reduce(lambda x, y: x + y, lt)
print(res)  # 15

# 计算列表元素之和
res = reduce(lambda x, y: x + y, lt, 10)  # 10为初始值
print(res)  # 25
