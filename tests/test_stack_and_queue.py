import pytest
from stack_and_queue.stack import Stack
from stack_and_queue.queue import Queue

# stack tests

# 1
def test_push_to_stack():
    stack_01=Stack()
    stack_01.push(1)
    actual = stack_01.__str__()
    expected = '1 -> None'
    assert actual == expected

# 2
def test_push_multi_values():
    stack_01=Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    actual = stack_01.__str__()
    expected = '3 -> 2 -> 1 -> None'
    assert actual == expected

# 3
def test_pop_stack():
    stack_01=Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    actual = stack_01.pop()
    expected = 3
    actual_2= stack_01.__str__()
    expected_2 = '2 -> 1 -> None'
    assert actual == expected
    assert actual_2 == expected_2

# 4
def test_is_empty_after_pops():
    stack_01=Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.pop()
    stack_01.pop()
    stack_01.pop()
    actual = stack_01.is_empty()
    expected = True
    assert actual == expected

# 5
def test_peek_stack():
    stack_01=Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    actual = stack_01.peek()
    expected = 3
    assert actual == expected

# 6
def test_empty_stack():
    stack_01=Stack()
    actual = stack_01.is_empty()
    expected = True
    assert actual == expected

# 7
def test_pop_or_peek_when_empty_stack():
    stack_01=Stack()
    with pytest.raises(Exception) as exception:
        stack_01.pop()
    expected_message = 'The stack is empty'
    
    with pytest.raises(Exception) as exception_2:
        stack_01.peek()
    expected_message = 'The stack is empty'

    assert str(exception.value) == expected_message
    assert str(exception_2.value) == expected_message

# queue tests

# 8
def test_enqueue_to_queue():
    q=Queue()
    q.enqueue("Asem")
    actual = q.__str__()
    expected = 'Asem -> None'
    assert actual == expected

# 9
def test_enqueue_multi_values():
    q=Queue()
    q.enqueue("Asem")
    q.enqueue("Omar")
    q.enqueue("Ahmad")
    actual = q.__str__()
    expected = 'Asem -> Omar -> Ahmad -> None'
    assert actual == expected

# 10
def test_dequeue():
    q=Queue()
    q.enqueue("Asem")
    q.enqueue("Omar")
    q.enqueue("Ahmad")
    actual = q.dequeue()
    expected = 'Asem'
    assert actual == expected

# 11
def test_peek_queue():
    q=Queue()
    q.enqueue("Asem")
    q.enqueue("Omar")
    q.enqueue("Ahmad")
    actual = q.peek()
    expected = 'Asem'
    assert actual == expected

# 12
def test_is_empty_after_dequeue():
    q=Queue()
    q.enqueue("Asem")
    q.enqueue("Omar")
    q.enqueue("Ahmad")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected

# 13
def test_empty_queue():
    q=Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected

# 14
def test_dequeue_or_peek_when_empty_queue():
    q = Queue()
    with pytest.raises(Exception) as exception:
        q.dequeue()
    expected_message = 'The queue is empty'
    
    with pytest.raises(Exception) as exception_2:
        q.peek()
    expected_message = 'The queue is empty'

    assert str(exception.value) == expected_message
    assert str(exception_2.value) == expected_message


  
 
