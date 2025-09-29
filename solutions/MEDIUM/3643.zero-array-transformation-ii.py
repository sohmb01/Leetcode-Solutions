# Problem ID: 3643
# Title: Zero Array Transformation II
# Runtime: 712 ms

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def canFormZeroes(k):
            diff = [0] * (n+1)
            total = 0
            for q in range(k):
                l,r,val = queries[q]
                diff[l] += val
                diff[r+1] -= val
            for i in range(n):
                total += diff[i]
                if total < nums[i]:
                    return False
            return True
        l,r = 0, len(queries)

        if not canFormZeroes(r):
            return -1
        
        while l<=r:
            m = (l+r)//2
            if canFormZeroes(m):
                r = m-1
            else:
                l = m+1

        return l