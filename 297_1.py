class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        res = []
        def DFS(root: TreeNode):
            if root is None:
                res.append("None")
                return
            else:
                res.append(str(root.val))
                DFS(root.left)
                DFS(root.right)
            return
        DFS(root)
        return ",".join(res)

    def deserialize(self, data):
        def DFS(dataList):
            if not dataList:
                return
            if dataList[0] == "None":
                dataList.pop(0)
                return None

            root = TreeNode(dataList[0])
            dataList.pop(0)
            root.left = DFS(dataList)
            root.right = DFS(dataList)
            return root
        dataList = data.split(",")
        return DFS(dataList)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    solution = Codec()
    res = solution.serialize(root)
    res1 = solution.deserialize(res)
    print(res1.val,res1.left.val,res1.right.val)