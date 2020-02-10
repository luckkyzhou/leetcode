from typing import List
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        trie = {}
        for word in words:
            t = trie
            for s in word:
                if s not in t: t[s] = {}
                t = t[s]
            t["end"] = True

        i, n = 0, len(S)
        intervals = []
        while i < n:
            t = trie
            idx = i
            while idx < n and S[idx] in t:
                t = t[S[idx]]
                idx += 1
                if "end" in t: intervals.append((i, idx-1))
            i += 1

        if not intervals: return S
        merges = []
        intervals.sort()
        left, right = intervals[0][0], intervals[0][1]
        for interval in intervals:
            if interval[0] > right + 1:
                merges.append((left, right))
                left = interval[0]
                right = interval[1]
            else:
                right = max(right, interval[1])
        merges.append((left, right))

        res = list(S)
        for merge in merges:
            res[merge[0]] = "<b>" + res[merge[0]]
            res[merge[1]] += "</b>"
        return "".join(res)

if __name__ == '__main__':
    solution = Solution()
    res = solution.boldWords(["e","cab","de","cc","db"],"cbccceeead")
    print(res)