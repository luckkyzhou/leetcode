# -*- coding: utf-8 -*-

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root: Node) -> Node:
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root