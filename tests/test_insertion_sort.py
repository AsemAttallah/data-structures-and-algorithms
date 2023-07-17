import pytest
from insertion_sort.insertion import insertion

# stack tests

# 1
def test_reverse_sorted():
    reverse_sorted = [20,18,12,8,5,-2]
    actual = insertion(reverse_sorted)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_few_uniques():
    few_uniques = [5,12,7,5,5,7]
    actual = insertion(few_uniques)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_nearly_sorted():
    nearly_sorted = [2,3,5,7,13,11]
    actual = insertion(nearly_sorted)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected



