# Problem ID: 2408
# Title: Number of People Aware of a Secret
# Runtime: 3 ms

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        share, mod = 0, 10**9 + 7
        for i in range(2,n+1):
            if i>delay:
                share = (share + dp[i-delay] + mod)%mod
            if i>forget:
                share = (share - dp[i-forget] + mod) % mod
            dp[i] = share
        know = 0
        for i in range(n-forget+1, n+1):
            know = (know + dp[i]) % mod
        return know