# Problem ID: 217
# Title: Contains Duplicate
# Runtime: 415 ms

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)