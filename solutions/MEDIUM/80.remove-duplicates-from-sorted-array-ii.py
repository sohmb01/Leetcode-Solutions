# Problem ID: 80
# Title: Remove Duplicates from Sorted Array II
# Runtime: 48 ms

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        cnt = 1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                cnt+=1
            else:
                cnt = 1
            if cnt<=2:
                nums[index] = nums[i]
                index+=1
        return index