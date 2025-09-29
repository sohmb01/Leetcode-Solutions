# Problem ID: 295
# Title: Find Median from Data Stream
# Runtime: 159 ms

class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []

    def addNum(self, num: int) -> None:
        if len(self.l) > len(self.r):
            heapq.heappush(self.r, num)
        else:
            heapq.heappush(self.l, -num)

        if self.l and self.r and -self.l[0] > self.r[0]:
            a,b = -heapq.heappop(self.l), heapq.heappop(self.r)
            heapq.heappush(self.r, a)
            heapq.heappush(self.l, -b)

    def findMedian(self) -> float:
        if len(self.l) == len(self.r):
            median = (-self.l[0]+self.r[0])/2.0
        else:
            median = -self.l[0]
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()