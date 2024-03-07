"""
迭代器
"""

from collections.abc import Iterable

for temp in "Python":
    print(temp)

# 判断是否可以迭代
print(isinstance("Python", Iterable))  # True
print(isinstance(100, Iterable))  # False


# 自定义可迭代对象的迭代器
class MyIterator(object):
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# 定义可迭代对象
class MyIterable(object):
    def __init__(self):
        self.items = list()

    # 实现__iter__方法，即为可迭代对象
    def __iter__(self):
        return MyIterator(self.items)

    def add(self, item):
        self.items.append(item)


my_iterable = MyIterable()
my_iterable.add("Python")
my_iterable.add("Java")
my_iterable.add("C++")

print(isinstance(my_iterable, Iterable))  # True

for temp in my_iterable:
    print(temp)
