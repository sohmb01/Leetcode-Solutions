# Problem ID: 1130
# Title: Last Stone Weight II
# Runtime: 15 ms

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = [0]*(total + 1)
        dp[0] = 1

        for weight in stones:
            for i in range(total,-1,-1):
                if i - weight < 0:
                    break
                if dp[i-weight]:
                    dp[i] = 1
        res = total + 1
        for s in range(1,total+1):
            if dp[s] and 2*s - total >= 0:
                res = min(res,2*s - total)
        return res