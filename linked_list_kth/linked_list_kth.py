class Node:
    '''
    This class to inheaerte nodes
    '''
    def __init__(self,value,next=None): 
        '''
        This is an initialization method to inheaerte nodes to give all node two things(value,next)
        '''
        self.value=value
        self.next=next

class LinkedList:
    '''
    This class to a Linked List 
    '''
    def __init__(self,head=None):
        '''
        This method to make an argument to put a head node on it
        '''
        self.head=head

    def traverse(self):
        '''
        This method to reach (traverse) all nodes
        '''
        current=self.head
        all_values=" "
        while current:
            all_values+=(current.value)+" "
            current=current.next
        return all_values
    
    def insert(self,value):
        '''
        This method to insert the new node, it's take one argument (value)
        '''
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
    
    def include(self,searched_vlaueal):
        '''
        This method to check if this argument (searched_vlaueal) is equal a value of some node or not
        '''
        current=self.head
        while current:
            if current.value==searched_vlaueal:
                return True
            current=current.next
        else:
            return False
    
    def to_string(self):
        '''
        This method to make output as that formated
        '''
        current=self.head
        string=""
        while current:
            string+= "{" + f" {current.value} " + "}"+ " -> "
            current=current.next
        string+=  " None" 
        return string
######
    def append_to_linked_list(self,appended_vlaue):
        '''
        This method to append a value as node to the linked list
        '''
        appended_node=Node(appended_vlaue)
        current=self.head
        while current:
            if current.next==None:
                current.next=appended_node
                return current.next
            current=current.next
    
    def insert_before(self,value_exist,inserted_value):
        '''
        This method to append a value as node before a specific value of node 
        '''
        inserted_node=Node(inserted_value)
        current=self.head
        
        while current:
            if current.value==value_exist:
                inserted_node.next=self.head
                self.head=inserted_node
                return self.head
            elif current.next.value==value_exist:
                inserted_node.next=current.next
                current.next=inserted_node
                return current
            current=current.next
    
    def insert_after(self,value_exist,inserted_value_after):
        '''
        This method to append a value as node after a specific value of node 
        '''
        inserted_node=Node(inserted_value_after)
        current=self.head
        while current:
            if current.value==value_exist:
                inserted_node.next=current.next
                current.next=inserted_node
                return current
            current=current.next
###
    def kth(self,k=0):
        current=self.head
        x=""
        y=0
        while current:
            y+=1
            z=y
            current=current.next
        else:
            if k<0 :
                raise IndexError("Negative value not accepted")
            elif 0<=k<z:
                current=self.head
                while current:
                    y-=1
                    if y==k:
                        x=(current.value)
                        return x 
                    current=current.next
            elif k==z:
                raise IndexError("length of list is equal to k")
            elif k>y:
                raise IndexError("Index out of range")
            

            
            
if __name__=="__main__":
    node3 = Node("studet03")
    node2 = Node("studet02", node3)
    node1 = Node("studet01", node2)
    linkedlist=LinkedList(node1)

    print(linkedlist.kth(-5))
        



    



