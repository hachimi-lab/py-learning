"""
Generics are a way to make your code more flexible and reusable. They allow you to write code that can work with any type, not just one specific type. This is useful when you want to write code that can work with different types of data, but you don't want to write the same code multiple times for each type.
"""
from typing import TypeVar

# T = TypeVar('T') # any type
T = TypeVar('T', int, float, str)


def func(a: T, b: T) -> T:
    return a + b


print(func(1, 2))  # 3
print(func(1.1, 2.2))  # 3.3000000000000003
print(func('a', 'b'))  # ab
