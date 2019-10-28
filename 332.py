from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hashmap = {}
        for start, target in tickets:
            hashmap.setdefault(start,[]).append(target)
        for start in hashmap.keys():
            hashmap[start].sort()

        res = []

        def DFS(start):
            while start in hashmap.keys() and hashmap[start]:
                DFS(hashmap[start].pop(0))
            res.append(start)

        DFS("JFK")
        return res[::-1]