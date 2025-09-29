# Problem ID: 3491
# Title: Find the Maximum Length of Valid Subsequence II
# Runtime: 905 ms

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(k):
            dp = [0]*k
            for num in nums:
                dp[num%k] = dp[(i-num)%k] + 1
            res = max(res,max(dp))
        return res