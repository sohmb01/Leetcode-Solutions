# Problem ID: 2050
# Title: Count Good Numbers
# Runtime: 0 ms

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        mod = 10 ** 9 + 7
        def mul(x,y):
            ret,mult = 1, x
            while y > 0:
                if y%2 == 1:
                    ret = ret * mult % mod
                mult = mult * mult % mod
                y = y//2
            return ret
            
        
        return mul(5,(n+1)//2) * mul(4,n//2) % mod