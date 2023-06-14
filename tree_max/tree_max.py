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
    
    def maximum_value(self):
        '''
        This method to find the maximum value of a node then return it 
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
        
        for x in output:
            if x>output[0]:
                output[0]=x
        return output[0]







if __name__=="__main__":
    tree=BinaryTree()
    tree.root=Tnode(10)
    tree.root.left=Tnode(200)
    tree.root.right=Tnode(5)
    tree.root.left.left=Tnode(30000000)
    tree.root.left.right=Tnode(40000)
    tree.root.right.left=Tnode(600000)
    # tree.add(10)
    # # tree.contains(15)
    # tr=BinarySearchTree()
    # tr.root=Tnode(20)
    # tr.root.left=Tnode(10)
    # tr.root.right=Tnode(50)
    # tr.add(15)
    # tr.add(20)
    # tr.add(30)
    # tr.add(40)
    # tr.add(50)
    # tr.add(60)
    # print(tree.breadth_first())
    # print(tree)
    # print(tree.root.value)
    # print(tree.pre_order())
    print(tree.maximum_value())
    # print(tr.contains(60))
    # print(tr.post_order())
    # print(tree.post_order())
    # print(tr.pre_order())
    # print(tr.contains(50))
    # print(tr.post_order())