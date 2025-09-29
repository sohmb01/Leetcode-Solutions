# Problem ID: 2882
# Title: Ways to Express an Integer as Sum of Powers
# Runtime: 286 ms

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            val = i**x
            if val > n:
                break
            for j in range(n, val-1, -1):
                dp[j] = (dp[j] + dp[j-val]) % mod
        return dp[n]