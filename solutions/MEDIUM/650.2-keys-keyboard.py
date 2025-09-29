# Problem ID: 650
# Title: 2 Keys Keyboard
# Runtime: 179 ms

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [num for num in range(n+1)]
        dp[1] = 0
        for num in range(2,n+1):
            for i in range(2,int(num//2)+1):
                if num % i == 0:
                    dp[num] = min(dp[num],dp[i]+num//i)
                    
        return dp[n]
