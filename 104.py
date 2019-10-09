# -*- coding: utf-8 -*-
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1