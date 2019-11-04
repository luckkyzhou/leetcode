from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(',',' ')
        paragraph = paragraph.replace('.',' ')
        paragraph = paragraph.replace('!',' ')
        paragraph = paragraph.replace('?',' ')
        paragraph = paragraph.replace(';',' ')
        paragraph = paragraph.replace('\'',' ')
        strings = paragraph.split()
        hashmap = {}
        for string in strings:
            if string not in banned:
                if string not in hashmap:
                    hashmap[string] = 1
                else:
                    hashmap[string] += 1
        m = 0
        for string in hashmap:
            if m < hashmap[string]:
                m = hashmap[string]
                res = string
        return res