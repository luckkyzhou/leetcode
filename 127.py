from typing import List
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or not beginWord or not wordList or endWord not in wordList: return 0

        # 将单词的带*匹配存入dict中
        L = len(beginWord)
        comboWordList = defaultdict(list)
        for word in wordList:
            for i in range(L):
                comboWordList[word[:i] + "*" + word[i + 1:]] += [word]

        queue = [(beginWord, 1)]
        visited = set(beginWord)
        while queue:
            curWord, level = queue.pop(0)
            for i in range(L):
                tempWord = curWord[:i] + "*" + curWord[i + 1:]
                for word in comboWordList[tempWord]:
                    if word == endWord: return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                comboWordList[tempWord] = []
        return 0