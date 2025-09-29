# Problem ID: 326
# Title: Power of Three
# Runtime: 12 ms

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        curr = 1
        while n > curr:
            curr*=3
            if curr == n:
                return True
        return True if n==1 else False