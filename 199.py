from typing import List
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        hashmap = {}
        def DFS(root, i):
            if not root:
                return
            hashmap[i] = root.val
            DFS(root.left, i + 1)
            DFS(root.right, i + 1)
        DFS(root, 0)
        return hashmap.values()