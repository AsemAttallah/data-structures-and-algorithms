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
    
class PseudoQueue:
    '''
    This class to inheaerte a pseudo queue
    '''
    def __init__(self,top=None):
        self.stack = Stack(top)
        self.stack_2 = Stack()

    def enqueue(self, value):
        '''
        This method to add a node in to a pseudo queue, it's take one argument (value)
        '''
        self.stack.push(value)
    
    
    def dequeue(self):
        '''
        This method to delete the node from the front return its value 
        '''
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
        This method to return all node in pseudo queue
        '''
        current=self.stack.top
        string=""
        while current:
            string+= "[" + f"{current.value}" + "]"+ " -> "
            current=current.next
        return string+"None"



if __name__=="__main__":   
    node4 = Node(20)
    node3 = Node(15, node4)
    node2 = Node(10,node3)
    node1 = Node(5,node2)
    pseudo_queue=PseudoQueue(node1)

    print(pseudo_queue.dequeue())
    print(pseudo_queue.__str__())

