class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.first = None
        self.last = None
        def DFS(root):
            if not root: return
            DFS(root.left)
            if self.last:
                self.last.right = root
                root.left = self.last
            else:
                self.first = root
            self.last = root
            DFS(root.right)
        DFS(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first