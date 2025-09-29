# Problem ID: 594
# Title: Longest Harmonious Subsequence
# Runtime: 53 ms

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,0
        res = 0
        n = len(nums)
        while r<n:
            while r<n and nums[r]-nums[l]<=1:
                r+=1
            if nums[r-1]-nums[l]==1:
                res = max(res,r-l)
            l+=1

            
        return res