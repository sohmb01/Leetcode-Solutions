# Problem ID: 532
# Title: K-diff Pairs in an Array
# Runtime: 2 ms

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        def findDuplicate(nums):
            nums.sort()
            n = len(nums)
            l, r = 0,1
            cnt = 0
            while r < n:
                while r<n and nums[r] == nums[r-1]:
                    r+=1
                if l != r-1:
                    cnt+=1
                l = r
                r = r+1

            return cnt
                

        if k==0:
            return findDuplicate(nums)

        s = set(nums)
        res = 0
        for num in s:
            if num+k in s:
                res+=1
        return res
