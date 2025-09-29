# Problem ID: 209
# Title: Minimum Size Subarray Sum
# Runtime: 15 ms

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        n = len(nums)
        curr = n+1
        s = nums[0]
        while l<=r and r<n:
            if s>=target:
                curr = min(curr, r-l+1)
                s-=nums[l]
                l+=1
                
            else:
                r+=1
                if r == n:
                    continue
                s+=nums[r]
        return 0 if curr == n+1 else curr
            