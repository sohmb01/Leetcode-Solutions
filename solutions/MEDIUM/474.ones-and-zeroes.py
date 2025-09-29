# Problem ID: 474
# Title: Ones and Zeroes
# Runtime: 1554 ms

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        def getBinDigits(s):
            z,o = 0,0
            for c in s:
                if c == "0":
                    z+=1
                else:
                    o+=1
            return z,o
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            z,o = getBinDigits(s)
            for i in range(m,z-1,-1):
                for j in range(n,o-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-z][j-o]+1)
        return dp[m][n]