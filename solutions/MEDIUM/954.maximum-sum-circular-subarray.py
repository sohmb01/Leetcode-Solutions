# Problem ID: 954
# Title: Maximum Sum Circular Subarray
# Runtime: 92 ms

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, minSum, maxSum, currMin, currMax = 0, float('inf'),-float('inf'),float('inf'),-float('inf')
        for num in nums:
            total+= num
            currMin = min(num,currMin+num)
            minSum = min(currMin, minSum)
            currMax = max(num,currMax+num)
            maxSum = max(maxSum, currMax)
        return max(maxSum,total-minSum) if maxSum>0 else maxSum