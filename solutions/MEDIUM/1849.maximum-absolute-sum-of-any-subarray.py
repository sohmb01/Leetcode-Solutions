# Problem ID: 1849
# Title: Maximum Absolute Sum of Any Subarray
# Runtime: 44 ms

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans, s = 0, 0
        minSum, maxSum = 0,0
        for num in nums:
            s += num
            minSum = min(minSum, s)
            maxSum = max(maxSum,s)
        return abs(maxSum - minSum)
