class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_bst(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    node = TreeNode(arr[mid])
    print(node.val)
    node.left = create_bst(arr, start, mid-1)
    node.left = create_bst(arr, mid+1, end)
    
    return node

def sorted_array_to_bst(arr):
    return create_bst(arr, 0, len(arr)-1)
    

arr = [1,2,3,4,5,6,7,8,9,11]
bst = sorted_array_to_bst(arr)
