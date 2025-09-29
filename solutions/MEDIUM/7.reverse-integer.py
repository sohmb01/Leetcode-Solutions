# Problem ID: 7
# Title: Reverse Integer
# Runtime: 46 ms

class Solution:
    def reverse(self, x: int) -> int:
        isNegative = True if x<0 else False
        x = abs(x)
        res = 0
        while x:
            digit = x%10
            x = x//10
            if (res > (2**31 - 1)//10) or (res == (2**31 - 1)//10 and digit>7):
                return 0 
            res = res*10 + digit
        return -res if isNegative else res