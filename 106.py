# -*- coding: utf-8 -*-

from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        return root