class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def DFS(root: TreeNode):
            if not root: return 0
            return DFS(root.left) + DFS(root.right) + 1
        return DFS(root)