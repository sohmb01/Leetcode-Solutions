# Problem ID: 62
# Title: Unique Paths
# Runtime: 4 ms

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i ==0 or j ==0:
                    dp[i][j] = 1
        for i in range(m):
            for j in range(n):
                if not (i ==0 or j ==0):
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

    