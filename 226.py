class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def recursion(root: TreeNode):
            if not root: return None
            recursion(root.left)
            recursion(root.right)
            root.left, root.right = root.right, root.left
            return root
        return recursion(root)