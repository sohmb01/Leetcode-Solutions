# Problem ID: 2478
# Title: Longest Nice Subarray
# Runtime: 93 ms

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        usedBits = 0
        start = 0
        for end in range(n):
            
            while nums[end] & usedBits !=0:
                usedBits ^= nums[start]
                start+=1
            usedBits |= nums[end]
            res = max(end-start+1,res)
        return res