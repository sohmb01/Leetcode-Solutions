# Problem ID: 215
# Title: Kth Largest Element in an Array
# Runtime: 95 ms

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums)-k +1):
            ans = heapq.heappop(nums)
        return ans