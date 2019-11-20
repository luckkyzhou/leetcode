class WordDictionary:
    def __init__ (self):
        self.hashmap = {}

    def addWord (self, word: str) -> None:
        self.hashmap[len(word)] = self.hashmap.get(len(word), []) + [word]

    def search (self, word: str) -> bool:
        def search(s):
            for i in range(len(word)):
                if word[i] != string[i] and word[i] != ".":
                    return False
            return True
        if len(word) not in self.hashmap: return False
        for string in self.hashmap[len(word)]:
            if search(string):
                return True
        return False