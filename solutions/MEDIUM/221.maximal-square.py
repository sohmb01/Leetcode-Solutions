# Problem ID: 221
# Title: Maximal Square
# Runtime: 171 ms

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols = len(matrix), len(matrix[0])
        dp = [ [0 for _ in range(cols+1)] for _ in range(rows+1)]
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1" :
                    dp[i+1][j+1] = min(min(dp[i][j],dp[i][j+1]),dp[i+1][j]) + 1
                maxArea = max(maxArea, dp[i+1][j+1])
        
        return maxArea ** 2
                
