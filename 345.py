class Solution:
    def reverseVowels(self, s: str) -> str:
        S = list(s)
        vowel = {"a","e","i","o","u","A","E","I","U","O"}
        p1 ,p2 = 0, len(s) - 1
        while p1 < p2:
            while S[p1] not in vowel and p1 < p2: p1 += 1
            while S[p2] not in vowel and p1 < p2: p2 -= 1
            if p1 < p2:
                S[p1], S[p2] = S[p2], S[p1]
                p1 += 1
                p2 -= 1
        return "".join(S)