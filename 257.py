from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        res = []
        def DFS(root: TreeNode, cur):
            if not root: return
            if not root.left and not root.right:
                cur += str(root.val)
                res.append(cur)
                return
            DFS(root.left, cur + str(root.val) + "->")
            DFS(root.right, cur + str(root.val) + "->")
        DFS(root, "")
        return res