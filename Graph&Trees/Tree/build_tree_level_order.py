class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def build_level_order(arr):
    if not arr: return
    
    queue = []
    node = TreeNode(arr[0])
    queue.append(node)
    index = 1
    
    while index < len(arr):
        current_node = queue.pop(0)
        
        if arr[index] is not None:
            left_node = current_node.left = TreeNode(arr[index])
            queue.append(left_node)
        index += 1
        
        if arr[index] is not None:
            right_node = current_node.right = TreeNode(arr[index])
            queue.append(right_node)
        index += 1
    return node
        

def print_level_order(root):
    if not root: return
    
    queue = [root]
    
    while queue:
        root = queue.pop(0)
        if root:
            print(root.val, end=' ')
            queue.append(root.left)
            queue.append(root.right)
        
            
            
        
arr = [6,2,8,0,4,7,9,None,None,3,5]
tree = build_level_order(arr)

print_level_order(tree)
