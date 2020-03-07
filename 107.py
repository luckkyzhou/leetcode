class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = [root]
        while queue:
            temp = []
            resNode = []
            for node in queue:
                resNode.append(node.val)
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            queue = temp
            res.insert(0, resNode)
        return res