import random
class RandomizedSet:
    def __init__(self):
        self.randomSet = set()

    def insert(self, val: int) -> bool:
        if val in self.randomSet: return False
        else:
            self.randomSet.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.randomSet: return False
        else:
            self.randomSet.remove(val)
            return True

    def getRandom(self) -> int:
        if not self.randomSet: return None
        else: return random.choice(list(self.randomSet))