class Tnode:
    '''
    This class to inheaerte nodes
    '''
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    '''
    This class to inheaerte a tree
    '''
    def __init__(self):
        '''
        This is an initialization method to inheaerte a properties toor with value none 
        '''
        self.root=None
    
    def pre_order(self):
        '''
        This method to make traversing (root,left,right)
        '''
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
        '''
        This method to make traversing (left,root,right)
        '''
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
        '''
        This method to make traversing (left,right,root)
        '''
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

class BinarySearchTree(BinaryTree):
    '''
    This class to inheaerte a binary search tree
    '''
    def add(self,value):
        '''
        This method to add a node in its appropriate position in tree, it takes one argument which is the value of added node
        '''
        def _walk(root):
            if root.value>=value:
                if root.left:
                    _walk(root.left)
                else:
                    root.left=Tnode(value)
            
            elif root.value<value:
                if root.right:
                    _walk(root.right)
                else:
                    root.right=Tnode(value)
        try:
            _walk(self.root)
        except:
            self.root=Tnode(value)

    def contains(self,find_value):
        '''
        This method to check if the value given as argument is exist in the nodes to return True or not to return False 
        '''
        def _finder(root):
            print(root.value)
            
            if root.value==find_value:
                return True

            elif root.value>find_value:
                if root.left:
                    return _finder(root.left)
            
            elif root.value<find_value:
                if root.right:
                    return _finder(root.right)
            
            return False
    
        return _finder(self.root)
        

        
    
            
        




if __name__=="__main__":
    # tree=BinaryTree()
    # tree.root=Tnode(10)
    # tree.root.left=Tnode(20)
    # tree.root.right=Tnode(50)
    # tree.root.left.left=Tnode(30)
    # tree.root.left.right=Tnode(40)
    # tree.root.right.left=Tnode(60)
    # tree.add(10)
    # tree.contains(15)
    tr=BinarySearchTree()
    tr.root=Tnode(20)
    tr.root.left=Tnode(10)
    tr.root.right=Tnode(50)
    tr.add(15)
    # tr.add(20)
    # tr.add(30)
    tr.add(40)
    # tr.add(50)
    # tr.add(60)
    # print(tree.breadth_first())
    # print(tree)
    # print(tree.root.value)
    # print(tree.pre_order())
    # print(tree.contains(20))
    print(tr.post_order())
    # print(tree.post_order())
    # print(tr.pre_order())
    # print(tr.contains(50))
    # print(tr.post_order())