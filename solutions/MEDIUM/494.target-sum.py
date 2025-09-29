# Problem ID: 494
# Title: Target Sum
# Runtime: 194 ms

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        def backtrack(i,s):
            if i == n :
                return 1 if s == target else  0
            if (i,s) in memo:
                return memo[(i,s)]
            memo[(i,s)] = backtrack(i+1,s+nums[i]) + backtrack(i+1,s-nums[i])
            return memo[(i,s)]
        return backtrack(0,0)
