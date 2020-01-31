from typing import List

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        senLen = 0
        for sen in sentence: senLen += len(sen) + 1

        index = 0
        res = 0
        for i in range(rows):
            cur = cols
            while cur > 0 and cur >= len(sentence[index]):
                cur -= len(sentence[index])
                index += 1
                if cur > 0: cur -=1
                if index == len(sentence):
                    res += cur / senLen + 1
                    cur %= senLen
                    index = 0

        return res