import heapq
class MedianFinder:
    def __init__ (self):
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum (self, num: int) -> None:
        heapq.heappush(self.minHeap, num)
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if len(self.minHeap) < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian (self) -> float:
        return float(self.minHeap[0]) if len(self.maxHeap) != len(self.minHeap) else (self.minHeap[0] - self.maxHeap[0]) / 2