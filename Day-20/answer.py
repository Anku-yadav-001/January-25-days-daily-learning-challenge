from collections import deque

class Codec:
    spliter = ","
    NN = "X"

    def serialize(self, root):
        def build_string(node, sb):
            if not node:
                sb.append(self.NN)
                sb.append(self.spliter)
            else:
                sb.append(str(node.val))
                sb.append(self.spliter)
                build_string(node.left, sb)
                build_string(node.right, sb)

        sb = []
        build_string(root, sb)
        return "".join(sb)

    def deserialize(self, data):
        def build_tree(nodes):
            val = nodes.popleft()
            if val == self.NN:
                return None
            else:
                node = TreeNode(int(val))
                node.left = build_tree(nodes)
                node.right = build_tree(nodes)
                return node

        nodes = deque(data.split(self.spliter))
        return build_tree(nodes)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
serialized = codec.serialize(root)
print("Serialized:", serialized)

deserialized = codec.deserialize(serialized)
print("Deserialized:", codec.serialize(deserialized))
