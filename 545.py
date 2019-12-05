from typing import List
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        if not root.left and not root.right: return [root.val]
        leftBoundary = []
        rightBoundary = []
        childNode = []

        if root.left: node = root.left
        else: node = None
        while node:
            if node.left or node.right: leftBoundary.append(node.val)
            else: break
            if node.left:
                node = node.left
                continue
            if node.right:
                node = node.right

        if root.right: node = root.right
        else: node = None
        while node:
            if node.left or node.right: rightBoundary.append(node.val)
            else: break
            if node.right:
                node = node.right
                continue
            if node.left:
                node = node.left

        def DFS(root):
            if not root: return
            if not root.left and not root.right: childNode.append(root.val)
            DFS(root.left)
            DFS(root.right)
        DFS(root)

        res = [root.val] + leftBoundary + childNode + rightBoundary[::-1]
        return res