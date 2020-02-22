class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        res = []
        def dfs(root: TreeNode):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            height = max(left, right)
            if height == len(res): res.append([])
            res[height].append(root.val)
            return height + 1
        dfs(root)
        return res