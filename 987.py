from typing import List
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        hashmap = {}
        def DFS(root, vertical, level):
            if not root: return
            hashmap[vertical] = hashmap.get(vertical, []) + [(root.val, level)]
            DFS(root.left, vertical - 1, level + 1)
            DFS(root.right, vertical + 1, level + 1)
        DFS(root, 0, 0)

        res = []
        sortHashmap = sorted(hashmap.items(), key=lambda x: x[0])
        for key, value in sortHashmap:
            value.sort(key=lambda x: (x[1],x[0]))
            temp = []
            for val in value:
                temp.append(val[0])
            res.append(temp)
        return res

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = solution.verticalTraversal(root)
    print(res)