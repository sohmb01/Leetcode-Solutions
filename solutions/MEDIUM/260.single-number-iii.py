# Problem ID: 260
# Title: Single Number III
# Runtime: 3 ms

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        setBit = xor & -xor
        a,b = 0,0
        for num in nums:
            if num & setBit:
                a ^= num
            else:
                b^=num
        return [a,b]
            