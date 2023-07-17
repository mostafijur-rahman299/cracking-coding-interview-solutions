class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def insert(root, val):
    if not root:
        root = TreeNode(val)
        return root
    
    if root.val > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
        
def array_to_bst(arr):
    root = None
    
    for item in arr:
        root = insert(root, item)
    return root
        
root = array_to_bst([5,1,3,4,7,2])

def search(root, key):
    if not root:
        return False
    
    if root.val > key:
        return search(root.left, key)
    elif root.val == key:
        return True
    else:
        return search(root.right, key)
    
    
search(root, 5)
