# Problem ID: 268
# Title: Missing Number
# Runtime: 113 ms

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        ans = 0
        for i in range(0,n+1):
            ans = ans ^ i
        for i in nums:
            ans = ans ^ i
        return ans