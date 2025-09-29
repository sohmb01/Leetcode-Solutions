# Problem ID: 2048
# Title: Build Array from Permutation
# Runtime: 1 ms

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]