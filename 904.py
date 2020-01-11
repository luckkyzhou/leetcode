from typing import List

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if tree == []: return 0

        count = 0
        left = 0
        res = 0
        hashmap = {}

        for right in range(0, len(tree)):
            hashmap[tree[right]] = hashmap.get(tree[right], 0) + 1
            if hashmap[tree[right]] == 1: count += 1

            while count > 2 and left < right:
                hashmap[tree[left]] -= 1
                if hashmap[tree[left]] == 0: count -=1
                left += 1
            res = max(res, right - left + 1)
        return res