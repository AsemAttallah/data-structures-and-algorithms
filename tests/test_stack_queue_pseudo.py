import pytest
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue,Stack,Node


# enqueue(value)
def test_sample_one_stack_queue_pseudo():
    node3 = Node(20)
    node2 = Node(15, node3)
    node1 = Node(10,node2)
    pseudo_queue=PseudoQueue(node1)
    # 10 -> 15 -> 20 -> None
    pseudo_queue.enqueue(5)
    actual = pseudo_queue.__str__()
    expected = "[5] -> [10] -> [15] -> [20] -> None"
    assert actual == expected

def test_sample_two_stack_queue_pseudo():
    pseudo_queue=PseudoQueue()
    pseudo_queue.enqueue(5)
    actual = pseudo_queue.__str__()
    expected = "[5] -> None"
    assert actual == expected


# dequeue()
def test_sample_three_stack_queue_pseudo():
    node4 = Node(20)
    node3 = Node(15, node4)
    node2 = Node(10,node3)
    node1 = Node(5,node2)
    pseudo_queue=PseudoQueue(node1)
    # [5] -> [10] -> [15] -> [20] -> None
    actual = pseudo_queue.dequeue()
    expected = 20
    assert actual == expected

def test_sample_four_stack_queue_pseudo():
    node3 = Node(15)
    node2 = Node(10,node3)
    node1 = Node(5,node2)
    pseudo_queue=PseudoQueue(node1)
    # [5] -> [10] -> [15] -> None
    actual = pseudo_queue.dequeue()
    expected = 15
    assert actual == expected