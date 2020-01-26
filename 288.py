from typing import List
from collections import defaultdict
class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.hashmap = defaultdict(list)
        for d in dictionary:
            if len(d) > 2:
                temp = d[0] + str(len(d[:-1])) + d[-1]
                self.hashmap[temp].append(d)
    def isUnique(self, word: str) -> bool:
        if word == "": return True
        temp = word[0] + str(len(word[:-1])) + word[-1]
        if temp in self.hashmap:
            if word not in self.hashmap[temp] or len(self.hashmap[temp]) > 1: return False
        return True

if __name__ == '__main__':
    solution = ValidWordAbbr(["deer","door","cake","card"])
    print(solution.isUnique("door"))