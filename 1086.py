from typing import List

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x: (x[0], -x[1]))
        res = []
        hashmap = {}
        for i in items:
            hashmap.setdefault(i[0], []).append(i[1])

        for index in hashmap:
            scores = hashmap[index]
            average = sum(scores[:5]) // 5
            res.append([index, average])
        return res