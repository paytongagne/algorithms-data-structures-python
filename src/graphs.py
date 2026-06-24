from __future__ import annotations

from collections import deque
from collections.abc import Hashable

Graph = dict[Hashable, list[Hashable]]


def breadth_first_search(graph: Graph, start: Hashable) -> list[Hashable]:
    if start not in graph:
        return []

    visited: set[Hashable] = set()
    order: list[Hashable] = []
    queue: deque[Hashable] = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return order


def depth_first_search(graph: Graph, start: Hashable) -> list[Hashable]:
    if start not in graph:
        return []

    visited: set[Hashable] = set()
    order: list[Hashable] = []

    def visit(node: Hashable) -> None:
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)
    return order
