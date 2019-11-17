from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {value:index for index,value in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if hashmap[word1[j]] > hashmap[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2): return False
        return True

if __name__ == '__main__':
    solution = Solution()
    res = solution.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz")
    print(res)