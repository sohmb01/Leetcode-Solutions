# Problem ID: 300
# Title: Longest Increasing Subsequence
# Runtime: 2039 ms

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        l = len(nums)
        dp = [1]*l
        ans = 1
        for i in range(1,l):
            j = i-1
            while j>=0:
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
                j-=1
            ans = max(dp[i],ans)
        
        return ans