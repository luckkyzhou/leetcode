class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = idx2 = -1
        res = 2 ** 31
        for i, word in enumerate(words):
            if word == word1:
                idx1 = i
                if idx2 >= 0: res = min(res, abs(idx1 - idx2))
            if word == word2:
                idx2 = i
                if idx1 >= 0 and idx1 != idx2: res = min(res, abs(idx1 - idx2))
        return res