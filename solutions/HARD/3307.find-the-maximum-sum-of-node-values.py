# Problem ID: 3307
# Title: Find the Maximum Sum of Node Values
# Runtime: 212 ms

class Solution:
    def getMaxSum(self, i, isEven, dp, k, nums):
        if i == len(nums):
            return 0 if isEven else -float('inf')
        if dp[i][isEven] != -1:
            return dp[i][isEven]
        
        noXorOperation = nums[i] + self.getMaxSum(i+1, isEven, dp, k, nums)
        xorOperation = (nums[i]^k) + self.getMaxSum(i+1, isEven^1, dp, k, nums)

        dp[i][isEven] = max(noXorOperation,xorOperation)
        return dp[i][isEven]


    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        dp = [[-1]*2 for _ in range(len(nums))]
        return self.getMaxSum(0,1,dp,k, nums)