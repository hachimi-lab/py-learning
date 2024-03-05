"""
function.py
"""
from typing import Callable


# 类型注解
def do_sum(a: int, b: int) -> int:
    return a + b


print(do_sum(1, 2))  # 3


def print_sum(func: Callable[[int, int], int], a: int, b: int) -> None:
    print(func(a, b))


print_sum(do_sum, 1, 2)  # 3
