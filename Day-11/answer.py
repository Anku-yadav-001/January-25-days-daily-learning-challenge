class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrderToTree(levelorder):
    if not levelorder or levelorder[0] == -1:
        return None

    root = Node(levelorder[0])
    nodes = [root]
    i = 1
    while nodes and i < len(levelorder):
        current = nodes.pop(0)

        if levelorder[i] != -1:
            current.left = Node(levelorder[i])
            nodes.append(current.left)
        i += 1

        if i < len(levelorder) and levelorder[i] != -1:
            current.right = Node(levelorder[i])
            nodes.append(current.right)
        i += 1
    return root

def targetSum(root, X):
    def inorder(node, nums):
        if not node:
            return
        inorder(node.left, nums)
        nums.append(node.val)
        inorder(node.right, nums)

    nums = []
    inorder(root, nums)

    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == X:
            return "Yes"
        elif current_sum < X:
            left += 1
        else:
            right -= 1
    return "No"

t = int(input())
for _ in range(t):
    levelorder = list(map(int, input().split()))
    X = int(input())
    root = levelOrderToTree(levelorder)
    result = targetSum(root, X)
    print(result)