from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root: return []
        def DFS(root, sum, cur):
            if not root: return
            if not root.left and not root.right and sum - root.val == 0:
                cur.append(root.val)
                res.append(cur)
                return
            DFS(root.left, sum - root.val, cur + [root.val])
            DFS(root.right, sum - root.val, cur + [root.val])
        DFS(root, sum, [])
        return res