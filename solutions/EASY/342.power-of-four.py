# Problem ID: 342
# Title: Power of Four
# Runtime: 0 ms

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        while n >= x:
            if n == x:
                return True
            x*=4
        return False