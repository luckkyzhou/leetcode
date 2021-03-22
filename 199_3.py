class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = dict()

        def DFS(node, i):
            if not node:
                return None
            res[i] = node.val
            DFS(node.left, i+1)
            DFS(node.right, i+1)

        DFS(root, 0)
        return res.values()
