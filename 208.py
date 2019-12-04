class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.keys():
                node = node[char]
            else:
                node[char] = {}
                node = node[char]
        node["end"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.keys():
                node = node[char]
            else:
                return False
        if "end" in node.keys():
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node.keys():
                node = node[char]
            else:
                return False
        return True