from typing import List

class Solution:
    def DFS(self, index, inversed, visited) -> bool:
        if visited[index] == 2: return True
        if visited[index] == 1: return False

        visited[index] = 2
        for precursor in inversed[index]:
            if self.DFS(precursor, inversed, visited):
                return True

        visited[index] = 1
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: return True

        # 这里要设置 3 个状态
        # 0 就对应 False ，表示结点没有访问过
        # 1 就对应 True ，表示结点已经访问过，在深度优先遍历结束以后才置为 1
        # 2 表示当前正在遍历的结点，如果在深度优先遍历的过程中，
        # 有遇到状态为 2 的结点，就表示这个图中存在环
        visited = [0 for _ in range(numCourses)]

        # 逆邻接表，存的是每个结点的前驱结点的集合
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # 1 在前，0 在后
        inversed = [set() for _ in range(numCourses)]
        for x, y in prerequisites:
            inversed[x].add(y)

        for i in range(numCourses):
            if self.DFS(i, inversed, visited): return False
        return True