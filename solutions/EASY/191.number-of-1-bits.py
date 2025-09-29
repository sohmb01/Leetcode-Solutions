# Problem ID: 191
# Title: Number of 1 Bits
# Runtime: 32 ms

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while(n):
            if n & 1:
                cnt+=1
            n>>=1
        return cnt