# Problem ID: 338
# Title: Counting Bits
# Runtime: 128 ms

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        if n==0:
            return [0]
        k=1
        ans[1]=1
        for i in range (2,n+1) :
            if i-k == k:
                ans[i]=1
                k=i
            else:
                ans[i]=ans[i-k]+ans[k]
        return ans
             