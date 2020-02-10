class Logger:

    def __init__ (self):
        self.hashmap = {}

    def shouldPrintMessage (self, timestamp: int, message: str) -> bool:
        if message not in self.hashmap:
            self.hashmap[message] = timestamp
            return True
        else:
            if timestamp - self.hashmap[message] >= 10:
                self.hashmap[message] = timestamp
                return True
            else:
                return False