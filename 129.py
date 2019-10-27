from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    sum = 0
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.DFS(root, root.val)
        return self.sum

    def DFS(self, root: TreeNode, cur: int):
        if not root.left and not root.right:
            self.sum += cur
            return
        if root.left:
            self.DFS(root.left, cur * 10 + root.left.val)
        if root.right:
            self.DFS(root.right, cur * 10 + root.right.val)