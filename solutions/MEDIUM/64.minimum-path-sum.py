# Problem ID: 64
# Title: Minimum Path Sum
# Runtime: 19 ms

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        dp = grid
        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        print(dp)
        return dp[rows-1][cols-1]