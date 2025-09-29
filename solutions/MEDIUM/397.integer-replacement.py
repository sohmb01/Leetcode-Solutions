# Problem ID: 397
# Title: Integer Replacement
# Runtime: 99 ms

class Solution:
    def integerReplacement(self, n: int) -> int:
        
        cnt = 0 
        if n == 1:
            return cnt
        if n % 2 == 0:
            return 1 + self.integerReplacement(n//2)
        else:
            return 1 + min(self.integerReplacement(n-1),self.integerReplacement(n+1))