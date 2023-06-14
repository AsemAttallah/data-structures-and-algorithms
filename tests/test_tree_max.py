import pytest
from tree_max.tree_max import Tnode,BinaryTree


# stack tests

# 1
def test_find_maximum_value_in_first():
    tree=BinaryTree()
    tree.root=Tnode(10000000)
    tree.root.left=Tnode(2000000)
    tree.root.right=Tnode(50000)
    tree.root.left.left=Tnode(3000)
    tree.root.left.right=Tnode(400)
    tree.root.right.left=Tnode(60)
    
    actual = tree.maximum_value()
    expected = 10000000
    assert actual == expected


def test_find_maximum_value_in_between():
    tree=BinaryTree()
    tree.root=Tnode(10)
    tree.root.left=Tnode(200)
    tree.root.right=Tnode(50000)
    tree.root.left.left=Tnode(3000)
    tree.root.left.right=Tnode(400)
    tree.root.right.left=Tnode(60)
    
    actual = tree.maximum_value()
    expected = 50000
    assert actual == expected




def test_find_maximum_value_in_end():
    tree=BinaryTree()
    tree.root=Tnode(10)
    tree.root.left=Tnode(200)
    tree.root.right=Tnode(5000)
    tree.root.left.left=Tnode(3000)
    tree.root.left.right=Tnode(400)
    tree.root.right.left=Tnode(6000000)
    
    actual = tree.maximum_value()
    expected = 6000000
    assert actual == expected