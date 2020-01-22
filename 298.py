class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = 0
    def longestConsecutive(self, root: TreeNode) -> int:
        def DFS(root: TreeNode, parent: TreeNode, length):
            if not root: return

            if root.val == parent.val + 1: length += 1
            else: length = 1
            self.res = max(self.res, length)
            DFS(root.left, root, length)
            DFS(root.right, root, length)
        DFS(root, TreeNode(-99999), 0)
        return self.res