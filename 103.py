from typing import List
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [(root, 1)]
        hashmap = {}

        while queue:
            node, level = queue.pop(0)
            hashmap[level] = hashmap.get(level, []) + [node.val]
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))

        res = []
        for level in hashmap.keys():
            if level % 2 == 1:
                res.append(hashmap[level])
            else:
                res.append(hashmap[level][::-1])
        return res