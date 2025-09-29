# Problem ID: 2144
# Title: Maximum Difference Between Increasing Elements
# Runtime: 0 ms

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = 0
        mn = nums[0]
        for i in range(1,len(nums)):
            res = max(res,nums[i]-mn)
            mn = min(mn,nums[i])
        
        return -1 if res == 0 else res