# data-structures-and-algorithms
## code challenge 10 : stack and queue

## Approach & Efficiency
* In this challenge I did not need to iterating just in one method (__str__) so it's time complexity is O(n), otherwise time complexity is O(1), And the space complexity is  O(1)
* Big O: space complexity = O(1)



## Solution
### stack 
    push:
    stack_01=Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    stack_01 : 4 -> 3 -> 2 -> 1 -> None
    
    pop: 
    stack_01.pop() => 4
    stack_01 : 3 -> 2 -> 1 -> None

    peek:
    stack_01.peek() => 3

    is_empty:
    stack_01.is_empty => False

### queue
    enqueue:
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q : 1 -> 2 -> 3 -> 4 -> None
    
    dequeue: 
    q.dequeue() : 2 -> 3 -> 4 -> None

    peek:
    q.peek() : 2

    is_empty:
    q.is_empty => False
