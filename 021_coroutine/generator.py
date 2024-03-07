"""
生成器
"""

# 方式一：使用数据生成规则定义生成器
nums = (x * 2 for x in range(10))

for num in nums:
    print(num)


# 方式二：使用yield关键字定义生成器
def fibonacci(all_num):
    a, b = 0, 1
    for i in range(all_num):
        yield a  # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a + b


for num in fibonacci(10):
    print(num)


# 方式三：使用send方法控制生成器
def moving_average():
    total = 0
    count = 0
    average = None
    while True:
        term = yield average  # 通过yield语句返回结果，并接收外部传入的值
        total += term
        count += 1
        average = total / count


# 实时计算移动平均值
mov_avg = moving_average()
next(mov_avg)
for val in [10, 20, 30, 40]:
    avg = mov_avg.send(val)
    print(f'Moving average of last {val} values: {avg}')
