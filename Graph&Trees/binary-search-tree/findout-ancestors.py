class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_ancestors(root, target):
    if not root:
        return []

    ancestors = []
    current = root

    while current:
        if current.val == target:
            return ancestors
        elif current.val < target:
            ancestors.append(current.val)
            current = current.right
        else:
            ancestors.append(current.val)
            current = current.left

    return []

# Example usage
# Create a sample binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

target_node = 5
ancestors = find_ancestors(root, target_node)

if ancestors:
    print(f"Ancestors of node {target_node}: {ancestors}")
else:
    print(f"Node {target_node} not found in the tree.")
