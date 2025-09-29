# Problem ID: 583
# Title: Delete Operation for Two Strings
# Runtime: 124 ms

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2 = len(word1),len(word2)
        dp = [[0]*(l1+1) for _ in range(l2+1)]
        for i in range(1,l2+1):
            for j in range(1,l1+1):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
        
        return l1 + l2 - 2*dp[l2][l1]
                    