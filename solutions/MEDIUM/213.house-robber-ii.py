# Problem ID: 213
# Title: House Robber II
# Runtime: 21 ms

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<4:
            return max(nums)
        a, b = 0, 0
        for i in range(len(nums)-1):
            a,b = b,max(a+nums[i],b)
        c = max(a,b)
        
        a, b = 0, 0
        for i in range(1,len(nums)):
            a,b = b,max(a+nums[i],b)
        d = max(a,b)
        return max(c,d)

