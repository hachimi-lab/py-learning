"""
sort方法用于对列表进行排序
"""

lt = [1, 3, 2, 4, 5]

# 升序排序（默认）
lt.sort(reverse=False)  # change the original list
print(lt)

# 降序排序（通过给定方法实现）
lt.sort(key=lambda x: -x)
print(lt)
