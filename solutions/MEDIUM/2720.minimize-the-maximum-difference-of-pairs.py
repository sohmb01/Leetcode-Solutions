# Problem ID: 2720
# Title: Minimize the Maximum Difference of Pairs
# Runtime: 361 ms

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        
        def getCount(threshold):
            cnt,i = 0,0
            while i < n-1:
                if nums[i+1]-nums[i]<=threshold:
                    cnt+=1
                    i+=1
                i+=1
            return cnt
        
        l,r = 0,nums[-1]-nums[0]
        while l<r:
            m = l + (r-l)//2
            if getCount(m) < p:
                l = m + 1
            else:
                r = m
        return l