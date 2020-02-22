class HitCounter(object):
    def __init__ (self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.queue = deque()

    def hit (self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.queue.appendleft(timestamp)

    def getHits (self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.queue and timestamp - self.queue[-1] + 1 > 300:
            self.queue.pop()
        return len(self.queue)