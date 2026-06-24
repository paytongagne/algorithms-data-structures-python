from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any


class Stack:
    def __init__(self) -> None:
        self._items: list[Any] = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("cannot pop from an empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("cannot peek an empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


class Queue:
    def __init__(self) -> None:
        self._items: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        self._items.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("cannot dequeue from an empty queue")
        return self._items.popleft()

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


@dataclass
class Node:
    value: Any
    next: "Node | None" = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def append(self, value: Any) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def to_list(self) -> list[Any]:
        values: list[Any] = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    def contains(self, value: Any) -> bool:
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
