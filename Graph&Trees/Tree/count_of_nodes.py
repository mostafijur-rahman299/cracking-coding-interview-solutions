class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder):
    if not preorder:
        return None

    val = preorder.pop(0)
    if val == -1:  # represents a null node
        return None

    node = TreeNode(val)
    node.left = build_tree(preorder)
    node.right = build_tree(preorder)

    return node


# Pre-order traversal: [2, 3, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
preorder = [2, 3, 4, -1, -1, 5, -1, -1, 3, 8, 6, -1, -1]

tree_root = build_tree(preorder)


def count_of_nodes(root):
    if not root:
        return 0
    
    left = count_of_nodes(root.left)
    right = count_of_nodes(root.right)
    
    return left + right + 1

print(count_of_nodes(tree_root))
