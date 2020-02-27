class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def DFS(root):
            if not root: return True
            left = DFS(root.left)
            right = DFS(root.right)
            if not root.left and not root.right:
                self.count += 1
                return True
            if root.left:
                if not (left and root.left.val == root.val):
                    return False
            if root.right:
                if not (right and root.right.val == root.val):
                    return False
            self.count += 1
            return True

        DFS(root)
        return self.count