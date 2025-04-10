class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)

    def find(self, val):
        return self._find(self.root, val)

    def _find(self, node, val):
        if node is None:
            return None
        if node.val == val:
            return node
        elif val < node.val:
            return self._find(node.left, val)
        else:
            return self._find(node.right, val)

    def subtree_size(self, node):
        if node is None:
            return 0
        return 1 + self.subtree_size(node.left) + self.subtree_size(node.right)

# Reading input
n = int(input().strip())
values = list(map(int, input().split()))
target = int(input().strip())

# Building BST
bst = BST()
for val in values:
    bst.insert(val)

# Finding target node and calculating subtree size
target_node = bst.find(target)
print(bst.subtree_size(target_node))
