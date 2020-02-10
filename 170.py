import collections
class TwoSum:
    def __init__ (self):
        self.hashmap = collections.defaultdict(int)

    def add (self, number: int) -> None:
        self.hashmap[number] += 1

    def find (self, value: int) -> bool:
        for key in self.hashmap:
            if value - key in self.hashmap:
                if value - key != key or self.hashmap[key] >= 2: return True
        return False