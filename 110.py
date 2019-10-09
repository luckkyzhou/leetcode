# -*- coding:utf-8 -*-
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res = self.isBST(root)[0]
        return res
    def isBST(self, root: TreeNode):
        if root is None:
            return True, 0
        leftBool, leftCount = self.isBST(root.left)
        rightBool, rightCount = self.isBST(root.right)
        return leftBool and rightBool and abs(leftCount - rightCount) <= 1, max(leftCount, rightCount) + 1

if __name__ == '__main__':
    solution = Solution()
    res = solution.isBalanced()