from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def linear_search(values: Sequence[T], target: T) -> int:
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values: Sequence[T], target: T) -> int:
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
