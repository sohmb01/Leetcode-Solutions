# Problem ID: 283
# Title: Move Zeroes
# Runtime: 48 ms

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,i=0,0
        n=len(nums)
        while i<n:
            if nums[i]!=0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
            i+=1
        