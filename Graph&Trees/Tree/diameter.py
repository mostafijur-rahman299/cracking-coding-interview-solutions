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
preorder = [2, 3, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]

tree_root = build_tree(preorder)

def height(root):
    if root is None:
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    
    my_height = max(leftHeight, rightHeight) + 1
    return my_height


def diameter(root):
    if root is None:
        return 0
    
    diameter1 = diameter(root.left)
    diameter2 = diameter(root.right)
    diameter3 = height(root.left) + height(root.right) + 1
    
    return max(diameter3, max(diameter1, diameter2))

print(diameter(tree_root))
