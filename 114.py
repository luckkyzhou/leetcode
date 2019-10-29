# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    last = TreeNode(None)
    def flatten(self, root: TreeNode) -> None:
        if not root: return
        if self.last:
            self.last.left = None
            self.last.right = root
        self.last = root
        # 复制右子树，防止下一节点篡改
        copy = root.right
        self.flatten(root.left)
        self.flatten(copy)
