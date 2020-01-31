class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        prev = 0
        res = 0
        for w in word:
            diff = abs(prev - keyboard.find(w))
            prev = keyboard.find(w)
            res += diff
        return res