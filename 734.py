from typing import List
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        for word1, word2 in zip(words1, words2):
            if word1 == word2: continue
            if [word1, word2] not in pairs and [word2, word1] not in pairs: return False
        return True