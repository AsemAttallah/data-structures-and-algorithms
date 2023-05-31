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
    
    def __str__(self):
        '''
        This method to make to return all values of nodes as that formated
        '''
        current=self.head
        string=""
        while current:
            string+= "{" + f"{current.value}" + "}"+ " -> "
            current=current.next
        string+=  "None" 
        return string
    
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


def zip_linked_list(ll_1,ll_2):
    '''
    This function to make zipping between two linked lists that tooks it as input and the output is zipped linked list.
    '''
    head_node=Node(ll_1.head.value)
    zipped_listlinkedlist=LinkedList(head_node)
    current_1=ll_1.head
    current_2=ll_2.head
    current_1=current_1.next

    while current_1 != None or current_2 != None :
                if current_2!=None:
                    zipped_listlinkedlist.append_to_linked_list(current_2.value)
                    current_2=current_2.next
                if current_1!=None:
                    zipped_listlinkedlist.append_to_linked_list(current_1.value)
                    current_1=current_1.next
    return zipped_listlinkedlist


    
          
            
if __name__=="__main__":
 
    node2 = Node(3)
    node1 = Node(1, node2)
    linkedlist_1=LinkedList(node1)

    node6 = Node(4)
    node5 = Node(9, node6)
    node4 = Node(5, node5)
    linkedlist_2=LinkedList(node4)
   
    print(zip_linked_list(linkedlist_1,linkedlist_2).__str__())

        



    



