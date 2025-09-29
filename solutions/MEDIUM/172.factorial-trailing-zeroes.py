# Problem ID: 172
# Title: Factorial Trailing Zeroes
# Runtime: 32 ms

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        k=5
        ans=0
        while(k <=n):
            ans+=n//k
            k=k*5
        
        return ans