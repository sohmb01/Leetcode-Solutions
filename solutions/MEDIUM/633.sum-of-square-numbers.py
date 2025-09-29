# Problem ID: 633
# Title: Sum of Square Numbers
# Runtime: 252 ms

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq=c**0.5
        i=0
        for i in range (int(sq)+1):
            b=(c-i**2)**0.5
            if b==int(b):
                return True
            
        return False
            