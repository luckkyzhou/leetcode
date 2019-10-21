from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    pathnumber = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        self.Sum(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.pathnumber

    def Sum(self, root: TreeNode, sum: int):
        if not root: return
        if sum - root.val == 0: self.pathnumber += 1
        self.Sum(root.left, sum - root.val)
        self.Sum(root.right, sum - root.val)