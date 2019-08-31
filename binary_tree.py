class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.val, end=' ')
        in_order_traversal(node.right)


def pre_order_traversal(node):
    if node is not None:
        print(node.val, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.val, end=' ')



'''
Binary tree as follows : 
            1
           / \
          2   3
         / \    
        4   5
 
 inorder traversal  : 4 2 5 1 3
 preorder traversal : 1 2 4 5 3
 posrorder traversal: 4 5 2 3 1      

'''
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

in_order_traversal(root)
print()
pre_order_traversal(root)
print()
post_order_traversal(root)


