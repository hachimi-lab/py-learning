"""
dict: key-value pair
"""

# 创建字典
d = {'name': 'Swaroop', 'age': 20}
print(d)

# 获取元素
print(d['name'])

# 添加元素
d['address'] = 'Kathmandu'
print(d)

# 删除元素
del d['address']
print(d)

# 获取所有键
print(d.keys())

# 获取所有值
print(d.values())

# 获取所有键值对
print(d.items())

# 判断键是否存在
print('name' in d)
