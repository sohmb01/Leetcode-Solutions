# Problem ID: 15
# Title: 3Sum
# Runtime: 784 ms

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        length = len(nums)
        while i<length-2:
            j = i+1
            k = length-1
            target = -nums[i]
            while j<k:
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                    
                elif nums[j] + nums[k] > target:
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
            while i<length-2 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return ans
                