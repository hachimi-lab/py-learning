"""
with 使用场景： 1. 文件读写 2. 网络请求 3. 数据库连接
"""

# 使用try...finally实现文件写入
f = None
try:
    f = open('test.txt', 'w')
    f.write('Hello, world!')
except IOError as e:
    print(f'IOError occurred: {e}')
finally:
    if f:
        f.close()

# 使用with实现文件写入
with open('test.txt', 'w') as f:
    f.write('Hello, world!')
