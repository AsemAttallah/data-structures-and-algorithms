class Tnode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def breadth_first(self): #Big O : O(w): w the maximum width in the tree
        if not self.root:
            return self.root
        
        output=[]
        queue=Queue()
        queue.enqueue(self.root)
        
        while not queue.is_empty():

            front=queue.dequeue()
            output.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)

        return output
    
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