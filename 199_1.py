from typing import List
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        queue = []
        queue.append(root)

        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return res