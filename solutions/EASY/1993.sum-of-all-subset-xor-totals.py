# Problem ID: 1993
# Title: Sum of All Subset XOR Totals
# Runtime: 0 ms

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        return res * 2** (len(nums)-1)

       