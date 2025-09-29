# Problem ID: 1878
# Title: Check if Array Is Sorted and Rotated
# Runtime: 0 ms

class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = 2
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                flag-=1
            if not flag:
                return False
        return (flag==2 and nums[-1]>=nums[0]) or (flag==1 and nums[-1]<=nums[0])