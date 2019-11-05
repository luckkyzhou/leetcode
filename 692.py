from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = {}
        for word in words:
            if word not in hashmap:
                hashmap[word] = 1
            else:
                hashmap[word] += 1
        dicts = sorted(hashmap.items(), key = lambda x: (-x[1], x[0]))
        res = []
        for key in dicts[:k]:
            res.append(key[0])
        return res