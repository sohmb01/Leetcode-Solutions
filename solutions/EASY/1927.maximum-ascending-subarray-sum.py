# Problem ID: 1927
# Title: Maximum Ascending Subarray Sum
# Runtime: 0 ms

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currSum = nums[0]
        ans = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                currSum+=nums[i]
            else:
                ans = max(ans,currSum)
                currSum = nums[i]
            ans = max(ans,currSum)
        ans = max(ans,currSum)
        return ans
        