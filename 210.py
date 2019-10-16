from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0: return [i for i in range(numCourses)]

        inversed = [set() for _ in range(numCourses)]
        for x, y in prerequisites:
            inversed[y].add(x)
        visited = [0 for _ in range(numCourses)]

        res = []
        for i in range(numCourses):
            if self.DFS(i, inversed, visited, res): return []
        return res

    def DFS(self, index, inversed, visited, res):
        if visited[index] == 2: return True
        if visited[index] == 1: return False

        visited[index] = 2
        for precursor in inversed[index]:
            if self.DFS(precursor, inversed, visited, res):
                return True
        visited[index] = 1
        res.append(index)
        return False