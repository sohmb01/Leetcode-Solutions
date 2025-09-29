# Problem ID: 2690
# Title: House Robber IV
# Runtime: 315 ms

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def isCapable(capability):
            i = 0
            housesRobbed = 0
            while i < n:
                if nums[i]<=capability:
                    housesRobbed+=1
                    i+=2
                else:
                    i+=1
            return housesRobbed >= k
        
        l,r = 1,max(nums)
        while l<r:
            m = (l+r)//2
            if isCapable(m):
                r = m
            else:
                l = m + 1
        return l
