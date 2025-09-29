# Problem ID: 3747
# Title: Maximum Difference Between Adjacent Elements in a Circular Array
# Runtime: 4 ms

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = abs(nums[-1]-nums[0])
        for i in range(1,len(nums)):
            diff = max(diff, abs(nums[i]-nums[i-1]))
        return diff