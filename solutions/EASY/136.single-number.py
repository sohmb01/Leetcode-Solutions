# Problem ID: 136
# Title: Single Number
# Runtime: 3 ms

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums[1:]:
            ans = ans^num
        return ans