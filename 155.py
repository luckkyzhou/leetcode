class MinStack:
    def __init__ (self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maximum = []

    def push (self, x: int) -> None:
        self.stack.append(x)
        if not self.maximum or (self.maximum and x <= self.maximum[-1]): self.maximum.append(x)

    def pop (self) -> None:
        if self.stack:
            temp = self.stack.pop()
            if self.maximum and temp == self.maximum[-1]:
                self.maximum.pop()

    def top (self) -> int:
        if self.stack: return self.stack[-1]

    def getMin (self) -> int:
        if self.maximum: return self.maximum[-1]

if __name__ == '__main__':
    minstack = MinStack()
    minstack.push(-2)
    minstack.push(0)
    minstack.push(-3)
    print(minstack.maximum)