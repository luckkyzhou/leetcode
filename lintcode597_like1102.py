class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    average = 0
    node = None
    def findSubtree(self, root):
        pass
    def DFS(self, root):
        if root is None:
            return 0, 0
        leftSum, leftSize = self.DFS(root.left)
        rightSum, rightSize = self.DFS(root.right)

        Sum = leftSum + rightSum + root.val
        Size = leftSize + rightSize + 1

        if not self.node or Sum / Size > self.average:
            self.node = root
            self.average = Sum / Size
        return Sum, Size