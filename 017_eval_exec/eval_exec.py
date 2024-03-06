"""
eval() 与 exec() 用于执行字符串类型的 Python 代码
eval() 用于执行一个表达式，并返回表达式的值
exec() 用于执行一个语句块，没有返回值
"""

# eval 不接受返回值，exec 接受返回值
a = eval('10 + 20')
print(a)

exec('b = 10 + 20')
print(b)

c = '''
def func():
    return 100
'''
exec(c)
print(func())
