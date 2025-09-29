# Problem ID: 3788
# Title: Maximum Unique Subarray Sum After Deletion
# Runtime: 0 ms

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        return sum(set([num for num in nums if num > 0]))