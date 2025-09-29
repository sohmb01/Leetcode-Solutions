# Problem ID: 16
# Title: 3Sum Closest
# Runtime: 351 ms

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        currSum = float('-inf')

        for i in range(n-2):
            l,r = i+1, n-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s-target) < abs(currSum - target) :
                    currSum = s
                if s < target:
                    l+=1
                elif s > target:
                    r-=1
                else:
                    return target
        return currSum

        return currSum