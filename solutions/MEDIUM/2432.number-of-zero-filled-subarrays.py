# Problem ID: 2432
# Title: Number of Zero-Filled Subarrays
# Runtime: 36 ms

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        nums += [1]
        for num in nums:
            if num == 0:
                curr += 1
            else:
                res += ((curr+1) * curr) // 2
                curr = 0
        return res
