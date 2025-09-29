# Problem ID: 413
# Title: Arithmetic Slices
# Runtime: 0 ms

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        curr, res = 0,0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                curr+=1
                res += curr
            else:
                curr = 0
        return res