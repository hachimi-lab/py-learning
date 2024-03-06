"""
Counter类是一个计数器，它是字典的子类，用于统计可哈希对象。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。
"""

from collections import Counter

s1 = "Hello World"
s2 = "Hello Captain"

# 通过setdefault方法，统计字符串中每个字符出现的次数
d = {}
for i in s1:
    d[i] = d.setdefault(i, 0) + 1
print(d)

# 通过Counter类，统计字符串中每个字符出现的次数
d = Counter(s1)
d.update(s2)
print(d)
