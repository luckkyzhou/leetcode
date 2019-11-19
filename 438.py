from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        hashmap = {}
        dict_p = dict(Counter(p))
        left, right = 0, 0

        while right < len(s):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            if hashmap == dict_p:
                res.append(left)
            if left == right - len(p) + 1:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    hashmap.pop(s[left])
                left += 1
            right += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.findAnagrams("cbaebabacd","abc")
    print(res)