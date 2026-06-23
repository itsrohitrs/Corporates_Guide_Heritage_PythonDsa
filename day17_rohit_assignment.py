# ==========================================
# DSA MODULE 4 - TREES & BST ASSIGNMENT
# ==========================================

# ==========================================
# Question 1
# Node, Root, Leaf, Height
# ==========================================

print("========== Question 1 ==========")

print("""
Node:
A node is a single element in a binary tree that stores data.

Root:
The root is the topmost node of the tree.

Leaf:
A leaf node is a node that has no children.

Height:
The height of a tree is the number of edges on the longest path
from the root to a leaf.

Given Tree:

          8
         / \\
        3   10
       / \\
      1   6

Root = 8

Leaf Nodes = 1, 6, 10

Height = 2
(8 -> 3 -> 1 or 8 -> 3 -> 6)
""")


# ==========================================
# TreeNode Class
# ==========================================

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ==========================================
# Build Tree for Traversals
# ==========================================

root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)


# ==========================================
# Question 2
# Inorder, Preorder, Postorder
# ==========================================

print("\n========== Question 2 ==========")

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


print("Inorder Traversal:")
inorder(root)
print()

print("Preorder Traversal:")
preorder(root)
print()

print("Postorder Traversal:")
postorder(root)
print()

print("""
Explanation:
Inorder traversal of a BST always gives sorted output because
it visits:
Left Subtree -> Root -> Right Subtree

According to BST rules:
Left < Root < Right
""")


# ==========================================
# Question 3
# BST Insertion
# ==========================================

print("\n========== Question 3 ==========")

print("""
BST Rule:
For every node:
- Values smaller than the node go to the left subtree.
- Values greater than the node go to the right subtree.
""")


def insert(node, data):

    if node is None:
        return TreeNode(data)

    if data < node.data:
        node.left = insert(node.left, data)

    elif data > node.data:
        node.right = insert(node.right, data)

    return node


# Testing BST Insertion

bst_root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst_root = insert(bst_root, value)

print("BST Created Successfully")


# ==========================================
# Question 4
# BST Deletion Cases
# ==========================================

print("\n========== Question 4 ==========")

print("""
Case 1: Leaf Node

Example:

    10
   /
  5

Delete 5

Simply remove the node.

----------------------------------

Case 2: Node with One Child

Example:

    10
   /
  5
 /
2

Delete 5

Connect parent directly to child.

Result:

    10
   /
  2

----------------------------------

Case 3: Node with Two Children

Example:

       50
      /  \\
    30    70
   / \\   / \\
 20  40 60  80

Delete 50

Replace 50 with its Inorder Successor.

----------------------------------

What is Inorder Successor?

The inorder successor is the smallest value
present in the right subtree.

For node 50:

Right Subtree:

       70
      / \\
    60   80

Smallest value = 60

So 60 is the inorder successor.

----------------------------------

Why do we use the Inorder Successor?

Because replacing a node with its inorder successor
preserves the BST property:

Left Subtree < Root < Right Subtree

Therefore the tree remains a valid BST after deletion.
""")