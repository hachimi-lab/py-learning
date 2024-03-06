"""
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
"""

lt = ['a', 'b', 'c', 'd', 'e']

# 索引从 0 开始
for i, v in enumerate(lt):
    print(f"index: {i}, value: {v}")

# 索引从 1 开始
for i, v in enumerate(lt, 1):
    print(f"index: {i}, value: {v}")
