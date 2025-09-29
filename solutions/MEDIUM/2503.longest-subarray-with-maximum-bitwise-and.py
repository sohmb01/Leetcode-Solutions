# Problem ID: 2503
# Title: Longest Subarray With Maximum Bitwise AND
# Runtime: 239 ms

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        def getSubarrayLength(i):
            if i in visit:
                return 0
            l,r = i,i
            while l>0 and nums[l-1]&nums[i] == nums[i]:
                visit.add(l)
                l-=1
            while r<len(nums)-1 and nums[r+1]&nums[i] == nums[i]:
                visit.add(r)
                r+=1
            
            return r-l+1
            
        mx = max(nums)
        indices = []
        for i,num in enumerate(nums):
            if num == mx:
                indices.append(i)
        visit = set()
        mxLen = 1
        for idx in indices:
            mxLen = max(mxLen, getSubarrayLength(idx))
        return mxLen