# Problem ID: 1586
# Title: Longest Subarray of 1's After Deleting One Element
# Runtime: 59 ms

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, z, res = 0,0,0
        for r in range(len(nums)):
            if nums[r] == 0:
                z+=1
            while z > 1:
                if nums[l] == 0:
                    z-=1
                l+=1
            res = max(res, r-l)
        return res