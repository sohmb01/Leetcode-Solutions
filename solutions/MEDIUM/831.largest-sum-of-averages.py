# Problem ID: 831
# Title: Largest Sum of Averages
# Runtime: 118 ms

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        
        dp = [[0]*(k+1) for _ in range(n+1)]

        for i in range(1,n+1):
            dp[i][1] = prefix[i]/float(i)
        
        for p in range(2,k+1):
            for i in range(p,n+1):
                mx = 0.0
                for j in range(p-1,i):
                    mx = max(mx,dp[j][p-1] + (prefix[i]-prefix[j])/float(i-j))
                dp[i][p] = mx
        return dp[n][k]
