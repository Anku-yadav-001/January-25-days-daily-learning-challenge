# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    # If either of the trees is null, return the other tree
    if not t1:
        return t2
    if not t2:
        return t1
    
    # Merge the nodes by summing their values
    t1.val += t2.val
    
    # Recursively merge the left and right children
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    
    return t1

########## HAPPY CODING ##########