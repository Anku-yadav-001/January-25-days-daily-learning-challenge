class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBST(root):
    def helper(node):
        if not node:
            return (float('inf'), float('-inf'), 0, True)
        
        left_min, left_max, left_size, is_left_bst = helper(node.left)
        right_min, right_max, right_size, is_right_bst = helper(node.right)
        
        if is_left_bst and is_right_bst and left_max < node.val < right_min:
            size = left_size + right_size + 1
            return (min(left_min, node.val), max(right_max, node.val), size, True)
        else:
            return (0, 0, max(left_size, right_size), False)
    
    return helper(root)[2]
