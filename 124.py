class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = - 2 ** 31
    def maxPathSum(self, root: TreeNode) -> int:
        self.getMax(root)
        return self.res
    def getMax(self, root: TreeNode):
        if not root:
            return 0
        left = max(0, self.getMax(root.left))
        right = max(0, self.getMax(root.right))
        self.res = max(self.res, root.val + left + right)
        return max(left, right) + root.val

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(10)
    root.left = TreeNode(9)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(8)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = solution.maxPathSum(root)
    print(res)