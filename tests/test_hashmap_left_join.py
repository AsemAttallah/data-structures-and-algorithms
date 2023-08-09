import pytest
from hashmap_left_join.hashmap_left_join import left_join
from hashmap_left_join.hash_table import HashTable


def test_left_join_same_keys_order():
    left_table=HashTable()
    left_table.set("diligent","employed")
    left_table.set("fond","enamored")
    right_table=HashTable()
    right_table.set("diligent","idle")
    right_table.set("fond","averse")

    actual = left_join(left_table,right_table)
    expected = [["diligent","employed","idle"],["fond","enamored","averse"]]
    assert actual == expected


def test_left_join_different_keys_order():
    left_table=HashTable()
    left_table.set("fond","enamored")
    left_table.set("diligent","employed")
    right_table=HashTable()
    right_table.set("diligent","idle")
    right_table.set("fond","averse")

    actual = left_join(left_table,right_table)
    expected = [["fond","enamored","averse"],["diligent","employed","idle"]]
    assert actual == expected


def test_left_join_not_found():
    left_table=HashTable()
    left_table.set("diligent","employed")
    left_table.set("fond","enamored")
    left_table.set("wrath","delight")
    right_table=HashTable()
    right_table.set("diligent","idle")
    right_table.set("fond","averse")

    actual = left_join(left_table,right_table)
    expected = [["diligent","employed","idle"],["fond","enamored","averse"],["wrath","delight",None]]
    assert actual == expected