# Problem ID: 90
# Title: Subsets II
# Runtime: 0 ms

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        i = 0
        while i < len(nums):
            start = len(ans)
            for j in range(len(ans)):
               ans.append(ans[j]+[nums[i]]) 
            i+=1
            while i<len(nums) and nums[i-1] == nums[i]:
                newStart = len(ans)
                for j in range(start,len(ans)):
                    ans.append(ans[j]+[nums[i]])
                start = newStart
                i+=1
        return ans