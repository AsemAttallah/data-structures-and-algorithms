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


class AnimalShelter:
    '''
    This class to inheaerte a queue
    '''
    def __init__(self,front_dog=None,back_dog=None,front_cat=None,back_cat=None):
        '''
        This is an initialization method to inheaerte queue then give all node two things(species,name,front,back)
        '''
        self.front_dog=front_dog
        self.back_dog=back_dog

        self.front_cat=front_cat
        self.back_cat=back_cat

    def enqueue(self,species,name):
        '''
        This method to add a node in to a queue, it's take one argument (value)
        '''
        self.species=species
        self.name=name
        value={species: name}
        if self.species=="dog":
            new_node_dog=Node(value)
            if self.back_dog==None:
                self.back_dog=new_node_dog
                self.front_dog=new_node_dog
                self.back_dog.next=None
            else:
                self.back_dog.next=new_node_dog
                self.back_dog=new_node_dog
    
        elif self.species=="cat":
            new_node_cat=Node(value)
            if self.back_cat==None:
                self.back_cat=new_node_cat
                self.front_cat=new_node_cat
                self.back_cat.next=None
            else:
                self.back_cat.next=new_node_cat
                self.back_cat=new_node_cat
        else:
            raise Exception ("wrong species, it's dog or cat")
    
    def dequeue(self,pref):
        '''
        This method to delete the node from the front return its value 
        '''
        if pref=="dog":
            temp_dog=self.front_dog
            self.front_dog=temp_dog.next
            temp_dog.next=None
            return temp_dog.value

        if pref=="cat":
            temp_cat=self.front_cat
            self.front_cat=temp_cat.next
            temp_cat.next=None
            return temp_cat.value


    def __str1__(self):
        '''
        This method to return all node in queue
        '''
        current_cat=self.front_cat
        string=""
        while current_cat:
            string+=f"{current_cat.value}"
            string+=" -> "
            current_cat=current_cat.next
        return string+"None" 
    
    def __str2__(self):
        '''
        This method to return all node in queue
        '''
        current_dog=self.front_dog
        string=""
        while current_dog:
            string+=f"{current_dog.value}"
            string+=" -> "
            current_dog=current_dog.next
        return string+"None"
    
if __name__=="__main__":
    q=AnimalShelter()
    q.enqueue("dog","11")
    q.enqueue("dog","22")
    # q.enqueue("dog","33")
    # q.enqueue("dog","44")
    # q.enqueue("cat","11")
    # q.enqueue("cat","22")
    # q.enqueue("Omar")
    # q.enqueue("Ahmad")
    # q.enqueue("Welcome")
    # # q.enqueue("bye")
    # print(q)
    print(q.dequeue("dog"))
    # print(q)
    # print(q.dequeue("cat"))
    # print(q.__str1__())
    print(q.__str2__())
    # q.dequeue()
    # q.dequeue()
    # print(q)
    # print(q.__str__())
    # print(q.dequeue())
    # print(q.peek())
    # print(q)
    # print(q.front.value)
    # print(q.is_empty())