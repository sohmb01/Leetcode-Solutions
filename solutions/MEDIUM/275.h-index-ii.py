# Problem ID: 275
# Title: H-Index II
# Runtime: 0 ms

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l,r = 0,n-1
        h = 0
        
        while l<=r:
            m = (l+r)//2
            length = n - m
            x = min(length, citations[m])
            h = max(h,x)
            if length < citations[m]:
                r = m-1
            else:
                l = m+1
        return h