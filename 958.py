class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = [root]
        stop = False
        while queue:
            temp = queue.pop(0)
            if temp.left:
                if stop: return False
                queue.append(temp.left)
            else:
                stop = True
            if temp.right:
                if stop: return False
                queue.append(temp.right)
            else:
                stop = True
        return True