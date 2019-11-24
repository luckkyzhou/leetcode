def read4(buf) -> int:
    pass
class Solution:
    def __init__(self):
        self.index = 0
        self.count = 0
        self.temp = ["a"] * 4
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while i < n:
            if self.index == 0: self.count = read4(self.temp)
            if self.count == 0: break

            while i < n and self.index < self.count:
                buf[i] = self.temp[self.index]
                self.index += 1
                i += 1
            if self.index == self.count: self.index = 0
        return i