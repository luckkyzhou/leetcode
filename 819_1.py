from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
        paragraph = paragraph.lower().split()
        hashmap = {}
        for word in paragraph:
            hashmap[word] = hashmap.get(word, 0) + 1

        res = ""
        count = 0
        for string in hashmap:
            if string not in banned:
                if count < hashmap[string]:
                    count = hashmap[string]
                    res = string
        return res