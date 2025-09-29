# Problem ID: 343
# Title: Integer Break
# Runtime: 0 ms

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [1] * (n+1)
        dp[2],dp[3] = 2,3

        for num in range(4,n+1):
            for k in range(2,num//2+1):
                dp[num] = max(dp[num],dp[k]*dp[num-k])
        return dp[n]

