class MaxStack:
    def __init__ (self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []

    def push (self, x: int) -> None:
        self.stack.append(x)
        if not self.maxStack or (self.maxStack and x > self.maxStack[-1]): self.maxStack.append(x)

    def pop (self) -> int:
        tmp = self.stack.pop()
        if self.maxStack[-1] == tmp: self.maxStack.pop()
        return tmp

    def top (self) -> int:
        return self.stack[-1]

    def peekMax (self) -> int:
        return self.maxStack[-1]

    def popMax (self) -> int:
        tmp = self.maxStack.pop()
        while self.stack:
            if tmp == self.stack.pop(): break
        return tmp