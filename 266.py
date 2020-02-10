class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        temp = set()
        for string in s:
            if string in temp: temp.remove(string)
            else: temp.add(string)
        return True if len(temp) <= 1 else False