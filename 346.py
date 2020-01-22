class MovingAverage:

    def __init__ (self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []
        self.sum = 0

    def next (self, val: int) -> float:
        if len(self.queue) == self.size:
            self.sum -= self.queue[0]
            self.queue.pop(0)
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)