# Problem ID: 91
# Title: Decode Ways
# Runtime: 0 ms

class Solution:
    def numDecodings(self, s: str) -> int:
    
        n = len(s)
        dp = [-1]*(n+1)
        def dfs(i):
            if i>=n:
                dp[i] = 1
                return 1
            if dp[i] != -1:
                return dp[i]
            if s[i] == '0':
                dp[i] = 0
                return 0
            if i<n-1 and ( s[i]=='1' or (s[i]=='2' and s[i+1] in "1234560")):
                dp[i] = dfs(i+1)+dfs(i+2)
            else:
                dp[i]= dfs(i+1)
            return dp[i]
        return dfs(0)
                