class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def BSTFromPreorder(arr, N, i=0):
    """
    Reconstructs a BST from its preorder traversal.

    Args:
        arr: The array containing the preorder traversal of the BST.
        N: The number of nodes in the BST.
        i: The current index in the preorder traversal array.

    Returns:
        The root of the reconstructed BST.
    """
    if i >= N or arr[i] == -1:
        return None

    root = TreeNode(arr[i])
    i += 1

    while i < N and arr[i] < root.val:
        i += 1

    root.left = BSTFromPreorder(arr, N, i)
    root.right = BSTFromPreorder(arr, N, i)

    return root

preorder = [5, 2, 4, 9, 10]
N = len(preorder)
root = BSTFromPreorder(preorder, N)

def levelOrder(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

levelOrder(root) 