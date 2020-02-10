from typing import List
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        wordset = set()
        for word in words: wordset.add(word)
        for i in range(len(text)):
            for j in range(i, len(text)):
                if text[i:j+1] in wordset: res.append([i, j])
        return res