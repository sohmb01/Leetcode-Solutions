# Problem ID: 477
# Title: Total Hamming Distance
# Runtime: 143 ms

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for bit in range(32):
            mask = 1 << bit
            z = o = 0
            for num in nums:
                if mask & num:
                    o+=1
                else:
                    z+=1
            res += z * o
        return res