# Problem ID: 665
# Title: Non-decreasing Array
# Runtime: 0 ms

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if cnt or (i>1 and i<len(nums)-1 and nums[i-2]>nums[i] and nums[i+1]<nums[i-1] ):
                    return False
                cnt = 1
            
        return True
