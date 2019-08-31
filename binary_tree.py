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


from collections import deque


def level_order_print(node):
    if node is None:
        return None
    q = deque()
    q.append(node)
    while q:
        new_node = q.popleft();
        print(new_node.val, end=' ')
        if new_node.left is not None:
            q.append(new_node.left)
        if new_node.right is not None:
            q.append(new_node.right)


def height_recursive(node):
    if node is None:
        return 0
    return 1 + max(height_recursive(node.left), height_recursive(node.right))

def height_non_recursive(node):
    # base case
    if node is None:
        return 0
    #use queue
    q = deque()

    #initialize height to 0
    height = 0

    #add root node to queue
    q.append(node)

    while True:
        node_count = len(q)
        if node_count == 0:
            return height

        #increment height on every level
        height += 1

        #while all node of current level are not process stay in this loop and add next level nodes
        while node_count > 0:

            node = q[0]
            q.popleft()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            node_count -= 1

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

level_order_print: 1 2 3 4 5
height is 3
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
print()
level_order_print(root)
print()
print("height of binary tree is: {}".format(height_recursive(root)))
print()
print("height of binary tree is: {}".format(height_non_recursive(root)))

