# -*- coding: utf-8 -*-

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode):
        if root == None:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            root = queue.pop(0)
            if root:
                res.append(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                res.append(None)
        return res

    def deserialize(self, data: list):
        if len(data) == 0:
            return None
        res = TreeNode(data[0])
        queue = []
        queue.append(res)
        i = 1
        while queue:
            cur = queue.pop(0)
            if cur == None:
                continue
            if data[i] != None:
                cur.left = TreeNode(data[i])
            else:
                cur.left = None
            if data[i + 1] != None:
                cur.right = TreeNode(data[i + 1])
            else:
                cur.right = None
            queue.append(cur.left)
            queue.append(cur.right)
            i += 2
        return res

if __name__ == '__main__':
    solution = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    res = solution.serialize(root)
    print(res)