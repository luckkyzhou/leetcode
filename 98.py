# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = self.isValid(root)
        return res

    def isValid(self, root: TreeNode, low, high) -> bool:
        low = float('-inf')
        high = float('inf')
        if not root: return True
        if not low < root.val < high: return False
        return self.isValid(root.left, low, root.val) and self.isValid(root.right, root.val, high)