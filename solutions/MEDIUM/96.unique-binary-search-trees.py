# Problem ID: 96
# Title: Unique Binary Search Trees
# Runtime: 0 ms

class Solution:
    def numTrees(self, n: int) -> int:
        
        def getNumTrees(num):
            trees = 0
            for i in range(num+1):
                trees += dp[i] * dp[num-i]
            return trees

        dp = [1 for _ in range (n+1)]
        for i in range(2,n+1):
            dp[i] = getNumTrees(i-1)
        return dp[n]
