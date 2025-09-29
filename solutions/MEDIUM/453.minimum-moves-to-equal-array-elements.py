# Problem ID: 453
# Title: Minimum Moves to Equal Array Elements
# Runtime: 252 ms

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=min(nums)
        s=0
        for i in nums:
            s+=(i-m)
        return s