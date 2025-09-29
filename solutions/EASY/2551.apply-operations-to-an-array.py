# Problem ID: 2551
# Title: Apply Operations to an Array
# Runtime: 223 ms

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i], nums[i+1] = nums[i]*2 , 0
        i = 0
        while i<n:
            if nums[i] == 0:
                j = i
                while j<n-1 and nums[j]==0:
                    j+=1
                nums[i],nums[j] = nums[j],nums[i]
            i+=1

        return nums