# Problem ID: 875
# Title: Longest Mountain in Array
# Runtime: 15 ms

class Solution:
    def longestMountain(self, nums: List[int]) -> int:
        mxLen = 0
        n = len(nums)
        left,right = [0]*n, [0]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                left[i] = left[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                right[i] = right[i+1]+1
            if right[i] and left[i]:
                mxLen = max(mxLen, right[i]+left[i]+1)
        return mxLen
        