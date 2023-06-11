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

class Tnode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def pre_order(self):
        
        output=[]
        
        def _walk(root):
            #root
            output.append(root.value)

            #left
            if root.left:
                _walk(root.left)

            #right
            if root.right:
                _walk(root.right)
        
        _walk(self.root)
        return output
    
    def in_order(self):
        output=[]
        def _walk(root):
            #left
            if root.left:
                _walk(root.left)

            #root
            output.append(root.value)

            #right
            if root.right:
                _walk(root.right)
        
        _walk(self.root)
        return output
    
    def post_order(self):
        
        output=[]
        def _walk(root):
            
            #left
            if root.left:
                _walk(root.left)

            #right
            if root.right:
                _walk(root.right)
            
            #root
            output.append(root.value)
            

        _walk(self.root)
        return output




if __name__=="__main__":
    tree=BinaryTree()
    tree.root=Tnode(10)
    tree.root.left=Tnode(20)
    tree.root.right=Tnode(50)
    tree.root.left.left=Tnode(30)
    tree.root.left.right=Tnode(40)
    tree.root.right.left=Tnode(60)

    # print(tree.breadth_first())
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())
    