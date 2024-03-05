"""
Lambda does not support type hinting, so we need to use `Callable` from `typing` module.
"""

from typing import Callable

add: Callable[[int, int], int] = lambda x, y: x + y
print(add(1, 2))  # 3
