from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def insertion_sort(values: Sequence[T]) -> list[T]:
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result


def merge_sort(values: Sequence[T]) -> list[T]:
    if len(values) <= 1:
        return list(values)

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return _merge(left, right)


def _merge(left: list[T], right: list[T]) -> list[T]:
    merged: list[T] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
