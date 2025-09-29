# Problem ID: 50
# Title: Pow(x, n)
# Runtime: 0 ms

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res = pow(x,n//2)
            res *= res
            if n%2:
                res*=x
            return res
        
        ans = pow(x,abs(n))
        if n<0:
            return 1/ans
        return ans
