# Problem ID: 63
# Title: Unique Paths II
# Runtime: 0 ms

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0]*(n+1)]*(m+1)
        if not obstacleGrid[0][0]:
            dp[1][1] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m][n]
                    
                
                        
            

        print(dp)
        return dp[m-1][n-1]
                    
                        
