# Problem ID: 2262
# Title: Solving Questions With Brainpower
# Runtime: 64 ms

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        dp = [0]* (n+1)
        mx = 0
        for i in range(n-1,-1,-1):
            p,b = questions[i]
            if i+b+1 >= n:
                solve = 0
            else:
                solve = dp[i+b+1]
            dp[i] = max(p+solve, dp[i+1])
        return dp[0]