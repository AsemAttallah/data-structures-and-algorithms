import pytest
from linked_list_zip.linked_list_zip import Node,LinkedList,zip_linked_list


def test_sample_one_linked_list_zip():
    node3 = Node(2)
    node2 = Node(3, node3)
    node1 = Node(1, node2)
    linkedlist_1=LinkedList(node1)

    node6 = Node(4)
    node5 = Node(9, node6)
    node4 = Node(5, node5)
    linkedlist_2=LinkedList(node4)

    actual = zip_linked_list(linkedlist_1,linkedlist_2)
    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> None"
    assert actual == expected


def test_sample_two_linked_list_zip():
    node2 = Node(3)
    node1 = Node(1, node2)
    linkedlist_1=LinkedList(node1)

    node6 = Node(4)
    node5 = Node(9, node6)
    node4 = Node(5, node5)
    linkedlist_2=LinkedList(node4)

    actual = zip_linked_list(linkedlist_1,linkedlist_2)
    expected = "{1} -> {5} -> {3} -> {9} -> {4} -> None"
    assert actual == expected

def test_sample_three_linked_list_zip():
    node3 = Node(2)
    node2 = Node(3, node3)
    node1 = Node(1, node2)
    linkedlist_1=LinkedList(node1)

    node5 = Node(9)
    node4 = Node(5, node5)
    linkedlist_2=LinkedList(node4)

    actual = zip_linked_list(linkedlist_1,linkedlist_2)
    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> None"
    assert actual == expected


def test_sample_four_linked_list_zip():
    node3 = Node(2)
    node2 = Node(3, node3)
    node1 = Node(1, node2)
    linkedlist_1=LinkedList(node1)

    node9 = Node(4,)
    node8 = Node(4,node9)
    node7 = Node(4,node8)
    node6 = Node(4,node7)
    node5 = Node(9,node6)
    node4 = Node(5, node5)
    linkedlist_2=LinkedList(node4)

    actual = zip_linked_list(linkedlist_1,linkedlist_2)
    expected = "{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> {4} -> {4} -> {4} -> None"
    assert actual == expected

