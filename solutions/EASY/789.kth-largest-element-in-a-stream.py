# Problem ID: 789
# Title: Kth Largest Element in a Stream
# Runtime: 14 ms


class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        self.heap = nums
        self.k  = k

    def add(self, val: int) -> int:
        flag = True
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
            flag = False
        if val > self.heap[0] and flag:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)