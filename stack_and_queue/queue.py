class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

class Queue:
    def __init__(self,front=None,back=None):
        self.front=front
        self.back=back
    def enqueue(self,value):
        new_node=Node(value)
        if self.back==None:
            self.back=new_node
            self.front=new_node
            self.back.next=None
        else:
            self.back.next=new_node
            self.back=new_node
    
    def dequeue(self):
        if self.front==None:
            raise Exception ("The queue is empty")
        else:
            temp=self.front
            self.front=temp.next
            temp.next=None
            return temp.value
    
    def peek(self):
        if self.front==None:
            raise Exception ("The queue is empty")
        else:
            return self.front.value
    
    def is_empty(self):
        if self.front==None or self.back==None:
            return True
        else:
            return False

    def __str__(self):
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
    # print(q)
    q.dequeue()
    # q.dequeue()
    # q.dequeue()
    print(q)
    # print(q.__str__())
    # print(q.dequeue())
    # print(q.peek())
    # print(q)
    # print(q.front.value)
    # print(q.is_empty())

    