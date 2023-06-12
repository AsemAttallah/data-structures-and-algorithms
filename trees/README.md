# Code challenge 15 : tree

## Approach & Efficiency
* I think I cat finish it in a little time but I faced some problems took with me more time to finish the challenge.
* In this challenge I used recursion to reach all nodes and if statement to make a specific conditions.
* Big O: space complexity = O(n) in Binary Tree methods
* Big O: space complexity = O(1) in Binary Search Tree methods
* Big O: time complexity = O(n) for all methods

## Solution

1. Binary Tree class:

        tree=BinarySearchTree()
        tree.root=Tnode(20)
        tree.root.left=Tnode(10)
        tree.root.right=Tnode(50)

        Output:
        tree.pre_order(): [20,10,50]
        tree.in_order(): [10,20,50]
        tree.post_order(): [10,50,20]


2. Binary Search Tree class:

* add 

        tree=BinarySearchTree()
        tree.root=Tnode(20)
        tree.root.left=Tnode(10)
        tree.root.right=Tnode(50)
        tree.add(15)
        tree.add(40)
        
        Output:
        tree.pre_order(): [20, 10, 15, 50, 40]
      
* contains

        tree=BinarySearchTree()
        tree.root=Tnode(20)
        tree.root.left=Tnode(10)
        tree.root.right=Tnode(50)
    
        tree.contains(10): True
        tree.contains(22): False
    


