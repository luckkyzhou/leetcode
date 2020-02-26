class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        from collections import defaultdict
        hashmap = defaultdict(list)
        res = []
        for i, word in enumerate(words):
            hashmap[word] += [i]
        for i in hashmap[word1]:
            for j in hashmap[word2]:
                if i != j: res.append(abs(i - j))
        return min(res)