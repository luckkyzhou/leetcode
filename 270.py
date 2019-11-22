class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.difference = float('inf')
        self.res = 0
        def DFS(root):
            if not root: return
            temp = abs(root.val - target)
            if temp < self.difference:
                self.difference = temp
                self.res = root.val
            DFS(root.left)
            DFS(root.right)
        DFS(root)
        return self.res