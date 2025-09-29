# Problem ID: 416
# Title: Partition Equal Subset Sum
# Runtime: 489 ms

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        total = total//2
        dp = [False] * (total+1)
        dp[0] = True
        for num in nums:
            for i in range(total,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
        return dp[total]