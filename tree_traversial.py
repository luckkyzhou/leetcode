class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def preOrder(self, root: TreeNode):
        if not root:
            return
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def levelOrder(self, root: TreeNode):
        queue = [root]
        while queue:
            temp = queue.pop(0)
            print(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    solution = Solution()
    solution.preOrder(root)