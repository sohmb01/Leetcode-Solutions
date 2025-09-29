# Problem ID: 1402
# Title: Count Square Submatrices with All Ones
# Runtime: 51 ms

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        res = 0
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1]:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                    res += dp[i][j]
        return res