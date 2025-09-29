# Problem ID: 967
# Title: Minimum Falling Path Sum
# Runtime: 18 ms

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[float('inf')] + row + [float('inf')] for row in matrix]
        n =  len(matrix)
        currRow = n - 2
        while currRow >= 0:
            for col in range(1,n+1):
                dp[currRow][col] += min(dp[currRow+1][col-1],dp[currRow+1][col],dp[currRow+1][col+1])
            currRow-=1
        
        return min(dp[0])