class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        cnt = 0
        while queue:
            cnt += 1
            node = queue.pop()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return cnt