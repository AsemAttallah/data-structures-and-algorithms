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
        This is an initialization method to inheaerte queue and give these properties an initial values(front_dog,back_dog,front_cat,back_cat)
        '''
        self.front_dog=front_dog
        self.back_dog=back_dog

        self.front_cat=front_cat
        self.back_cat=back_cat

    def enqueue(self,species,name):
        '''
        This method to add a node in to a queue, it's take two arguments (species,name)
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
    
    def dequeue(self,pref):
        '''
        This method to delete the node from the front of its queue and return its value 
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
        
        if pref!="cat" or pref!="dog":
            return None
 

   