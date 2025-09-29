# Problem ID: 540
# Title: Single Element in a Sorted Array
# Runtime: 0 ms

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l,r = 0,len(nums)-1
        while l<r:
            m = (l+r)//2
            if m%2 == 1:
                m-=1
            if nums[m] == nums[m+1]:
                l = m+2
            else:
                r = m
        return nums[l]
