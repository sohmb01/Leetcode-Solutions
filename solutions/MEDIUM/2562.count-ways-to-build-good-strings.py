# Problem ID: 2562
# Title: Count Ways To Build Good Strings
# Runtime: 175 ms

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        dp = {}
        def backtrack(l):
            if l> high:
                return 0
            if l in dp:
                return dp[l]
            dp[l] = 1 if l>=low else 0
            dp[l] += backtrack(l+zero) + backtrack(l+one)
            return dp[l]%mod
        return backtrack(0)