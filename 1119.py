class Solution:
    def removeVowels(self, S: str) -> str:
        vowel = ["a", "e", "i", "o", "u"]
        for s in vowel: S = S.replace(s,"")
        return S