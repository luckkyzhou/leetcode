from typing import List
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def DFS(root):
            if not root: return
            DFS(root.left)
            res.append(root.val)
            DFS(root.right)
        return res