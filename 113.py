# -*- coding: utf-8 -*-
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    res = []
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        self.DFS(root, sum, [])
        return self.res

    def DFS(self, root, sum, cur):
        if not root: return
        if not root.left and not root.right and sum - root.val == 0:
            cur.append(root.val)
            self.res.append(cur)
            return
        self.DFS(root.left, sum - root.val, cur + [root.val])
        self.DFS(root.right, sum - root.val, cur + [root.val])