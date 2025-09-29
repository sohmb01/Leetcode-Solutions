# Problem ID: 1025
# Title: Minimum Cost For Tickets
# Runtime: 3 ms

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n+1)

        for i in range(n-1,-1,-1):
            j = i
            dp[i] = float("inf")
            for cost, duration in zip(costs,[1,7,30]):
                while j<n and days[j]<days[i]+duration:
                    j+=1
                dp[i] = min(dp[i],cost+dp[j])
        return dp[0]