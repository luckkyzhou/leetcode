class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BSTIterator:
    def __init__ (self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
    def next (self) -> int:
        cur = self.stack.pop()
        res = cur.val
        cur = cur.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res

    def hasNext (self) -> bool:
        return self.stack != []
