# Problem ID: 378
# Title: Kth Smallest Element in a Sorted Matrix
# Runtime: 23 ms

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        maxheap = []
        for row in matrix:
            for num in row:
                heappush(maxheap, -num)
                if len(maxheap) > k:
                    heappop(maxheap)
        return -maxheap[0]