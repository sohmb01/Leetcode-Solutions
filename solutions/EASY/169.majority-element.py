# Problem ID: 169
# Title: Majority Element
# Runtime: 168 ms

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=1
        ele=nums[0]
        for i in range(len(nums)):
            if ele==nums[i]:
                count+=1
            else:
                count-=1
            if count==0:
                ele=nums[i]
                count=1
        return ele