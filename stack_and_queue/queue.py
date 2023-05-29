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

class Queue:
    '''
    This class to inheaerte a queue
    '''
    def __init__(self,front=None,back=None):
        '''
        This is an initialization method to inheaerte queue then give all node two things(fron,back)
        '''
        self.front=front
        self.back=back
    def enqueue(self,value):
        '''
        This method to add a node in to a queue, it's take one argument (value)
        '''
        new_node=Node(value)
        if self.back==None:
            self.back=new_node
            self.front=new_node
            self.back.next=None
        else:
            self.back.next=new_node
            self.back=new_node
    
    def dequeue(self):
        '''
        This method to delete the node from the front return its value 
        '''
        if self.front==None:
            raise Exception ("The queue is empty")
        else:
            temp=self.front
            self.front=temp.next
            temp.next=None
            return temp.value
    
    def peek(self):
        '''
        This method to return the value of a front node  
        '''
        if self.front==None:
            raise Exception ("The queue is empty")
        else:
            return self.front.value
    
    def is_empty(self):
        '''
        This method to check if queue is empty or not
        '''
        if self.front==None or self.back==None:
            return True
        else:
            return False

    def __str__(self):
        '''
        This method to return all node in queue
        '''
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None" 
    
if __name__=="__main__":
    q=Queue()
    q.enqueue("Asem")
    q.enqueue("Omar")
    q.enqueue("Ahmad")
    # q.enqueue("Welcome")
    # # q.enqueue("bye")
    print(q)
    # q.dequeue()
    # q.dequeue()
    # q.dequeue()
    # print(q)
    # print(q.__str__())
    print(q.dequeue())
    # print(q.peek())
    print(q)
    # print(q.front.value)
    # print(q.is_empty())