class Node: 
    '''
    This class represent a node in linked list or other data structure
    has two main component the value of the node and the reference to the next node.
    arg: value
    return: None
    '''
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
    
class LinkedList:
    '''
    '''
    def __init__(self,head=None):
        self.head=head 
    
    def insert(self,value):
        '''
        This method using to insert a new node at the beginning  of the linked list
        arg: value
        return: None
        '''
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

class HashTable:
    '''
    It is a data structure that store key-value pairs of data 
    using buckets to increase data accessing efficiency
    '''
    def __init__(self,size=1024):
        self.__size=size
        self.__buckets=[None] * size
        self.all_keys=[]
        self.all_values_in_same_key=[]
        self.all_keys_values=[]
    
    def __hash(self,key):
        '''
        A method used to return the hash code of the given key
        arg:key
        return : hash code of the key(index)
        '''
        code=0
        for char in key:
            code+=ord(str(char))
        code*=283
        code = code % self.__size
        return code 

    def set(self,key,value):
        '''
        A method used to set key-value pair in the bucket, handling collisions as needed.
        args:
          key: The key which is hashed and used as the identifier for the value
          value : The value that is associated with a key
        return None
        '''
        index= self.__hash(key)
        if self.__buckets[index] is None:
            ll=LinkedList()
            self.__buckets[index]=ll
        self.__buckets[index].insert([key,value])
        self.all_keys.append(key)
        self.all_keys_values.append([key,value])
        
    def get(self,key):
        '''
        Retrieve the value with the given key from the hashtable
        arg: key
        return : value or none
        '''
        index=self.__hash(key)
        bucket=self.__buckets[index]

        if bucket is not None :
            current=bucket.head
            while current :
                if current.value[0]==key:
                    return current.value[1]
                current=current.next
        return None

    def has(self,key):
        '''
        A method to check if the given key is existed in thee hashtable
        arg: key
        return : boolean
        '''
        if self.get(key):
            return True
        return False

    def keys(self):
        '''
        arg: none
        Return a list of all the keys present in the hash table
        '''
        return self.all_keys
    
    def get_all_values_in_key(self,key):
        '''
        Retrieve all values with the given key from the hashtable
        arg: key
        return : all values with same key
        '''
        index=self.__hash(key)
        bucket=self.__buckets[index]
        current=bucket.head
        while current :
            if current.value[0]==key:
                self.all_values_in_same_key.append(current.value[1])
                current=current.next
        return self.all_values_in_same_key
    
    def keys_values(self):
        '''
        arg: none
        Return a list of all the keys and values present in the hash table
        '''
        return self.all_keys_values
    
if __name__=="__main__":
    hash=HashTable()
    hash.set("a","b")
    hash.set("a","g")
    hash.set("e","f")
    hash.set("g","h")
    
    # print(hash.get_all_values_in_key("a"))
    # print(self.__buckets[index])
    # print(hash.get_all_values_in_key("a"))
    # print(hash.get(hash.keys()[1]))
    # print("ell")
    print(hash.keys())