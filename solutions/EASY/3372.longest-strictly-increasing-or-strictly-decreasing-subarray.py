# Problem ID: 3372
# Title: Longest Strictly Increasing or Strictly Decreasing Subarray
# Runtime: 3 ms

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc,dec,cnt = 0,0,0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                cnt+=1
            else:
                cnt = 0
            inc = max(cnt,inc)
        cnt =0 
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                cnt+=1
            else:
                cnt = 0
            inc = max(cnt,inc)
        return inc+1 