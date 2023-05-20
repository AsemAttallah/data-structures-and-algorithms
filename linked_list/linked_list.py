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

        



# if __name__=="__main__":
#     node3=Node("studet03")
#     node2=Node("studet02",node3)
#     node1=Node("studet01",node2)

#     linkedlist=LinkedList(node1)
#     # print(LinkedList(node1).to_string())
#     # linkedlist=LinkedList(node1)
#     # print(LinkedList(node1).head.value)
#     # print(head)
#     # linkedlist.insert("studet047")
#     # LinkedList(node1).append_to_linked_list("ddd")
#     # print(linkedlist.traverse())
#     # LinkedList(node1).insert_before("studet02","kkkk")
#     # LinkedList(node1).insert_after("studet03","kkkk")
#     # print(linkedlist.kth(2))
#     print(linkedlist.kth(-2))
#     # print(linkedlist.traverse())
#     # print(node1.next.value)
#     # print(linkedlist.traverse())
#     # print(LinkedList(node1).include("studet03"))

    



