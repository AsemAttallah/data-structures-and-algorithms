import pytest
from linked_list.linked_list import Node,LinkedList

@pytest.fixture # This fixture used to make each test independet on other test 
def setup_linked_list():
    node3 = Node("studet03")
    node2 = Node("studet02", node3)
    node1 = Node("studet01", node2)
    return LinkedList(node1)

def test_empty_linked_list():
    '''
    This test to check if we can create an empty Linked List
    '''
    actual = LinkedList().head
    expected = None
    assert actual == expected

def test_insert_linked_list(setup_linked_list):
    '''
    This test to check if insert method is worked
    '''
    linkedlist=setup_linked_list
    linkedlist.insert("studet04")
    actual = linkedlist.traverse()
    expected = " studet04 studet01 studet02 studet03 "
    assert actual == expected
   
def test_head_first_value(setup_linked_list):
    '''
    This test to check if insert method is worked
    '''
    linkedlist=setup_linked_list
    actual = linkedlist.head.value
    expected = "studet01"
    assert actual == expected

def test_multi_nodes(setup_linked_list):
    '''
    This test to check if linked_list can include many nodes 
    '''
    linkedlist=setup_linked_list
    actual =linkedlist.traverse()
    expected = " studet01 studet02 studet03 "
    assert actual == expected

def test_find_value(setup_linked_list):
    '''
    This test to check if a value exist in a node 
    '''
    linkedlist=setup_linked_list
    actual = linkedlist.include("studet03")
    expected = True
    assert actual == expected

def test_did_not_find_value(setup_linked_list):
    '''
    This test to check if a value didn't exist in a node 
    '''
    linkedlist=setup_linked_list
    actual = linkedlist.include("studet06")
    expected = False
    assert actual == expected

def test_all_values(setup_linked_list):
    '''
    This test to check if output formated as required
    '''
    linkedlist=setup_linked_list
    actual = linkedlist.to_string()
    expected = "{ studet01 } -> { studet02 } -> { studet03 } ->  None"
    assert actual == expected

