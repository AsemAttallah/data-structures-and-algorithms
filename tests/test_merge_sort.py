import pytest
from merge_sort.merge_sort import merge_sort

# Reverse-sorted: [20,18,12,8,5,-2]
# Few uniques: [5,12,7,5,5,7]
# Nearly-sorted: [2,3,5,7,13,11]
def test_reverse_sorted():
    reverse_sorted = [20,18,12,8,5,-2]
    actual = merge_sort(reverse_sorted)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_few_uniques():
    few_uniques = [5,12,7,5,5,7]
    actual = merge_sort(few_uniques)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_nearly_sorted():
    nearly_sorted = [2,3,5,7,13,11]
    actual = merge_sort(nearly_sorted)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected