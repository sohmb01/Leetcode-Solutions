# Problem ID: 2998
# Title:   Count Symmetric Integers
# Runtime: 431 ms

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for num in range(low,high+1):
            s = str(num)
            if len(s) % 2:
                continue
            l,r = 0,len(s)-1
            diff = 0
            while l<r:
                diff+= int(s[l])
                diff-= int(s[r])
                l+=1
                r-=1
            if not diff:
                cnt+=1
        return cnt