# Problem ID: 198
# Title: House Robber
# Runtime: 41 ms

class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0,0
        for i in range(len(nums)):
            a, b = b, max(a+nums[i],b)
        return max(a,b)