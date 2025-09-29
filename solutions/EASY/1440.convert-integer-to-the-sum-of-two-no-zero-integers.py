# Problem ID: 1440
# Title: Convert Integer to the Sum of Two No-Zero Integers
# Runtime: 0 ms

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def isNoZero(x):
            return "0" not in str(x)

        for i in range(1,n):
            if isNoZero(i) and isNoZero(n-i):
                return [i,n-i]
    