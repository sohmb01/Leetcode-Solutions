# Problem ID: 324
# Title: Wiggle Sort II
# Runtime: 8 ms

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = ((len(nums)+1)//2)-1, len(nums)-1
        temp = sorted(nums)
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = temp[l]
                l-=1
            else:
                nums[i] = temp[r]
                r-=1

