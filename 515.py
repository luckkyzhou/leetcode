from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        hashmap = {}
        def DFS(root: TreeNode, depth: int):
            if not root: return
            if depth not in hashmap.keys() or root.val > hashmap[depth]:
                hashmap[depth] = root.val
            DFS(root.left, depth + 1)
            DFS(root.right, depth + 1)
        DFS(root, 0)
        res = []
        for value in hashmap.values():
            res.append(value)
        return res
