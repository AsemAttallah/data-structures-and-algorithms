class Node:
    '''
    This class to inheaerte nodes
    '''
    def __init__(self,value=None,next=None):
        '''
        This is an initialization method to inheaerte nodes to give all node two things(value,next)
        '''
        self.value=value
        self.next=next

class Stack:
    '''
    This class to inheaerte a stack
    '''
    def __init__(self,top=None):
        '''
        This is an initialization method to inheaerte stack to give it a (top)
        '''
        self.top=top
    
    def push(self,value):
        '''
        This method to push a node in to stack,it's take one argument (value)
        '''
        node = Node(value)
        if self.top==None:
            self.top=node
            self.top.next=None
        else:
            node.next=self.top
            self.top=node

    def pop(self):
        '''
        This method to delete the node from the top return its value  
        '''
        if self.top==None:
            raise Exception ("The stack is empty")
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
            return temp.value
        
    def peek(self):
        '''
        This method to return the value of a top node  
        '''
        if self.top==None:
            raise Exception ("The stack is empty")
        else:
            return self.top.value

    def is_empty(self):
        '''
        This method to check if stack is empty or not
        '''
        if self.top==None:
            return True
        else:
            return False

    def __str__(self):
        '''
        This method to return all node in stack
        '''
        current=self.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"
    
class PseudoQueue:
    def __init__(self,top=None):
        self.stack = Stack(top)
        self.stack_2 = Stack(top)

    def enqueue(self, value):
        self.stack.push(value)
    
    
    def dequeue(self,value):
        if self.stack.top==None:
            raise Exception ("The pseudo queue is empty")
        else:
            while self.stack.top!=None:
                value = self.stack.pop()
                self.stack_2.push(value)
            dequeued_value = self.stack_2.pop()

            while self.stack_2.top!=None:
                value = self.stack_2.pop()
                self.stack.push(value)
            
            return dequeued_value
        
    def __str__(self):
        '''
        This method to return all node in stack
        '''
        current=self.stack.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"



if __name__=="__main__":
    # stack_01=Stack()
    # stack_02=Stack()
    pseudo_queue=PseudoQueue()
    pseudo_queue2=PseudoQueue()

    # pseudo_queue.push("asem")
    pseudo_queue.enqueue("omar")
    pseudo_queue.enqueue("Ahmad")
    pseudo_queue.enqueue("essa")
    # pseudo_queue2.enqueue("Ahmad")
    # pseudo_queue2.enqueue("essa")
    # stack_01.push(2)
    # stack_01.push(3)
    # stack_02.push("hfg")
    # stack_02.push("ewr")
    # pseudo_queue.push(2)
    # print(stack_01.top)
    print(pseudo_queue)
    print(pseudo_queue.dequeue("essa"))
    # stack_01.push(4)
    # print(stack_01)
    # print(stack_02)
    # print(stack_01.pop())
    # print(stack_01)
    # print(stack_01.is_empty())
    # print(stack_01.peek())
    # print(stack_01.top.value)
    # print(stack_01.pop())
    # print(stack_01)

