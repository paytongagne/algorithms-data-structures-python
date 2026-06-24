from src.sorting import insertion_sort, merge_sort


def test_insertion_sort_orders_values():
    values = [5, 2, 4, 1, 3]
    assert insertion_sort(values) == [1, 2, 3, 4, 5]


def test_insertion_sort_does_not_mutate_original_list():
    values = [3, 1, 2]
    insertion_sort(values)
    assert values == [3, 1, 2]


def test_merge_sort_orders_values():
    values = [9, 7, 5, 3, 1]
    assert merge_sort(values) == [1, 3, 5, 7, 9]


def test_merge_sort_handles_empty_list():
    assert merge_sort([]) == []
