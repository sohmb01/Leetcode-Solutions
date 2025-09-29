# Problem ID: 53
# Title: Maximum Subarray
# Runtime: 559 ms

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        s = 0
        for num in nums:
            s = max(num,num+s)
            ans = max(ans,s)
        return ans