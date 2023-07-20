class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def insert(root, val):
    if not root:
        return TreeNode(val)

    if root.val > val:
        root.left = insert(root.left, val)
    elif root.val < val:
        root.right = insert(root.right, val)
    return root

def array_to_bst(arr):
    if not arr:
        return None
    
    root = None
    for item in arr:
        root = insert(root, item)
        
    return root

root = array_to_bst([5,1,3,4,7,2])


def in_order_traversing(root):
    if not root:
        return
    
    in_order_traversing(root.left)
    print(root.val)
    in_order_traversing(root.right)
    
in_order_traversing(root)


def delete(root, val):
    if root.val > val:
        root.left = delete(root.left, val)
    elif root.val < val:
        root.right = delete(root.right, val)
    else: # root.val == val
        # case 1
        if root.left == None and root.right == None:
            return None
        elif root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        
        inOrderSuccessor = in_order_successor(root.right)
        root.data = inOrderSuccessor.data
        root.right = delete(root.right, inOrderSuccessor.data)
        
    return root

def in_order_successor(root):
    while root.left:
        root = root.left
    return root

delete(root, 4)

in_order_traversing(root)
