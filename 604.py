class StringIterator:
    def __init__ (self, compressedString: str):
        self.string = compressedString
        self.idx = 0
        self.temp = 1
        self.num = 0
        while self.idx + self.temp < len(self.string) and self.string[self.idx + self.temp].isnumeric():
            self.num *= 10
            self.num += int(self.string[self.idx + self.temp])
            self.temp += 1

    def next (self) -> str:
        if not self.hasNext(): return " "
        if self.num == 0:
            self.idx += self.temp
            self.temp = 1
            while self.idx + self.temp < len(self.string) and self.string[self.idx + self.temp].isnumeric():
                self.num *= 10
                self.num += int(self.string[self.idx + self.temp])
                self.temp += 1
        self.num -= 1
        return self.string[self.idx]

    def hasNext (self) -> bool:
        if self.idx + self.temp == len(self.string) and self.num == 0: return False
        else: return True

if __name__ == '__main__':
    stringit = StringIterator("x6")
    print(stringit.next())
