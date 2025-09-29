# Problem ID: 2792
# Title: Neighboring Bitwise XOR
# Runtime: 49 ms

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x = 0
        for num in derived:
            x = x^num
        return x == 0