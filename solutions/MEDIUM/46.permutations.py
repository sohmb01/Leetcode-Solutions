# Problem ID: 46
# Title: Permutations
# Runtime: 3 ms

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ans = []
        for i in range(len(nums)):
            temp = [nums[i]]
            ret = self.permute(nums[:i]+nums[i+1:])
            for l in ret:
                ans.append(temp+l)
        return ans