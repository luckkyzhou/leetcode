class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        parent, parentRight = None, None
        while root:
            parentLeft = root.left
            root.left = parentRight
            parentRight = root.right
            root.right = parent
            parent = root
            root = parentLeft
        return parent