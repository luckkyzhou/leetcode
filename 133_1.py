class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    hashmap = {}
    def cloneGraph(self, node: Node) -> Node:
        return self.DFS(node)
    def DFS(self, node: Node):
        if not node: return
        if node in self.hashmap:
            return self.hashmap[node]

        clone = Node(node.val, [])
        self.hashmap[node] = clone
        for n in node.neighbors:
            clone.neighbors.append(self.DFS(n))
        return clone