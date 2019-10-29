class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    max = -(2 ** 31)
    res = 0
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.DFS(root, 0)
        return self.res

    def DFS(self, root: TreeNode, depth: int):
        if not root: return
        if not root.left and not root.right:
            if self.max < depth:
                self.max = depth
                self.res = root.val
        self.DFS(root.left, depth + 1)
        self.DFS(root.right, depth + 1)