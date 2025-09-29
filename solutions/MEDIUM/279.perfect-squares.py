# Problem ID: 279
# Title: Perfect Squares
# Runtime: 2142 ms

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [10001] * (n+1)
        i=1
        while i*i <= n:
            dp[i*i] = 1
            i+=1
        
        squares = []
        for i in range(1,n+1):
            if dp[i] == 1:
                squares.append(i)
                continue
            for square in squares:
                dp[i] = min(dp[i],dp[i-square]+dp[square])
        
        return dp[n]