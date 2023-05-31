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


def zip_linked_list(ll_1,ll_2):
    '''
    This function to make zipping between two linked lists that tooks it as input and the output is zipping all value in the two linked lists 
    '''
    current_1=ll_1.head
    current_2=ll_2.head
    count_1=0
    count_2=0
    stringg=""
    while current_1:
            count_1+=1
            current_1=current_1.next
    while current_2:
            count_2+=1
            current_2=current_2.next

    if count_1>=count_2:
        current_1=ll_1.head
        current_2=ll_2.head
        while current_1:
                if current_1!=None:
                    stringg+= "{" + f"{current_1.value}" + "}"+ " -> "
                    current_1=current_1.next
                if current_2!=None:
                    stringg+= "{" + f"{current_2.value}" + "}"+ " -> "
                    current_2=current_2.next
        return stringg+"None"   
    else:
        current_1=ll_1.head
        current_2=ll_2.head
        while current_2:
                if current_1!=None:
                    stringg+= "{" + f"{current_1.value}" + "}"+ " -> "
                    current_1=current_1.next
                if current_2!=None:
                    stringg+= "{" + f"{current_2.value}" + "}"+ " -> "
                    current_2=current_2.next
        return stringg+"None"
       

            
            
if __name__=="__main__":
    
    node3 = Node(2)
    node2 = Node(3, node3)
    node1 = Node(1, node2)
    linkedlist_1=LinkedList(node1)
    node6 = Node(4)
    node5 = Node(9, node6)
    node4 = Node(5, node5)
    linkedlist_2=LinkedList(node4)
    
    # node2 = Node(3)
    # node1 = Node(1, node2)
    # linkedlist_1=LinkedList(node1)

    # node6 = Node(4)
    # node5 = Node(9, node6)
    # node4 = Node(5, node5)
    # linkedlist_2=LinkedList(node4)

    # node3 = Node(2)
    # node2 = Node(3, node3)
    # node1 = Node(1, node2)
    # linkedlist_1=LinkedList(node1)

    # node9 = Node(4,)
    # node8 = Node(4,node9)
    # node7 = Node(4,node8)
    # node6 = Node(4,node7)
    # node5 = Node(9,node6)
    # node4 = Node(5, node5)
    # linkedlist_2=LinkedList(node4)


    print(zip_linked_list(linkedlist_1,linkedlist_2))

        



    



