class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    """
    Finds the kth smallest value in a Binary Search Tree (BST).

    Args:
        root: Root node of the BST.
        k: Index of the element to find.

    Returns:
        The value of the kth smallest node in the BST.
    """

    def inorder_traversal(node, k):
        if not node:
            return None

        left_result = inorder_traversal(node.left, k)
        if left_result:
            return left_result

        k -= 1
        if k == 0:
            return node.val

        return inorder_traversal(node.right, k)

    return inorder_traversal(root, k)

result = kthSmallest(root, 3) 
print(result)