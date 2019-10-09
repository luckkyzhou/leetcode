# -*- coding: utf-8 -*-
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    def isMirror(self, leftNode: TreeNode, rightNode: TreeNode) -> bool:
        if leftNode is None and rightNode is None:
            return True
        elif leftNode is None or rightNode is None or leftNode.val != rightNode.val:
            return False
        return self.isMirror(leftNode.right, rightNode.left) and self.isMirror(leftNode.left, rightNode.right)