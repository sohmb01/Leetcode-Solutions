# Problem ID: 69
# Title: Sqrt(x)
# Runtime: 3032 ms

class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while (True):
            if i*i==x:
                ans=i
                break
            if i*i>x:
                ans=i-1
                break
            i+=1
        return ans