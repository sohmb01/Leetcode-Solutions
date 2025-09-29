# Problem ID: 462
# Title: Minimum Moves to Equal Array Elements II
# Runtime: 76 ms

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums)//2]
        return sum(abs(i - median) for i in nums)