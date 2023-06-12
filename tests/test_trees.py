import pytest
from trees.trees import Tnode,BinaryTree,BinarySearchTree

# 1.Can successfully instantiate an empty tree
def test_empty_tree():
    tree=BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected

# 2.Can successfully instantiate a tree with a single root node
def test_tree_with_single_root():
    tree=BinaryTree()
    tree.root=Tnode(10)
    actual = tree.pre_order()
    expected = [10]
    assert actual == expected

# 3.For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_Binary_Search_Tree_add_left_right():
    tree=BinarySearchTree()
    tree.root=Tnode(20)
    tree.root.left=Tnode(10)
    tree.root.right=Tnode(50)
    tree.add(15)
    tree.add(40)
    actual = tree.pre_order()
    expected = [20, 10, 15, 50, 40]
    assert actual == expected

# 4.Can successfully return a collection from a pre-order traversal
def test_return_pre_order():
    tree=BinarySearchTree()
    tree.root=Tnode(20)
    tree.root.left=Tnode(10)
    tree.root.right=Tnode(50)
    tree.add(15)
    tree.add(40)
    actual = tree.pre_order()
    expected = [20, 10, 15, 50, 40]
    assert actual == expected

# 5.Can successfully return a collection from an in-order traversal
def test_return_in_order():
    tree=BinarySearchTree()
    tree.root=Tnode(20)
    tree.root.left=Tnode(10)
    tree.root.right=Tnode(50)
    tree.add(15)
    tree.add(40)
    actual = tree.in_order()
    expected = [10, 15, 20, 40, 50]
    assert actual == expected

# 6.Can successfully return a collection from a post-order traversal
def test_return_post_order():
    tree=BinarySearchTree()
    tree.root=Tnode(20)
    tree.root.left=Tnode(10)
    tree.root.right=Tnode(50)
    tree.add(15)
    tree.add(40)
    actual = tree.post_order()
    expected = [15, 10, 40, 50, 20]
    assert actual == expected

# 7.Returns true,false for the contains method, given an existing or non-existing node value
def test_return_True_False():
    tree=BinarySearchTree()
    tree.root=Tnode(20)
    tree.root.left=Tnode(10)
    tree.root.right=Tnode(50)
   
    actual_True = tree.contains(10)
    actual_False = tree.contains(25)
   
    expected_Ture = True
    expected_False = False
    
    assert actual_True == expected_Ture
    assert actual_False == expected_False
