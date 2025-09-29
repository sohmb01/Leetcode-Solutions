# Problem ID: 1335
# Title: Maximum Candies Allocated to K Children
# Runtime: 257 ms

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        def canDistribute(c):
            maxChildren = 0
            for candy in candies:
                maxChildren += candy//c
            return maxChildren>=k
        
        s = sum(candies)
        if s <= k:
            return s//k
        
        l,r = 0, max(candies)
        while l<r:
            m = (l+r+1)//2
            if canDistribute(m):
                l = m
            else:
                r = m-1
        return l
