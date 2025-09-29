# Problem ID: 31
# Title: Next Permutation
# Runtime: 0 ms

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1 2 3 5 4   1 2 4 3 5   1 2 4 5 3     1 2 5 3 4    1 2 5 4 3
        #  1 2 4 5 3     1 2 4 3 5     1 2 5 3 4
        n = len(nums)
        i = n - 2
        while i>=0 and nums[i] >= nums[i+1]:
            i-=1
        if i>=0:
            j = n -1
            while nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        nums[i+1:] = reversed(nums[i+1:])