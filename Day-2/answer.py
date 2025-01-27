
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insertNode(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insertNode(root.left, value)
    else:
        root.right = insertNode(root.right, value)
    return root

def maxDepth(root):
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)
