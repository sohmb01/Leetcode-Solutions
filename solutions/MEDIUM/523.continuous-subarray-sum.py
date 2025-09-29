# Problem ID: 523
# Title: Continuous Subarray Sum
# Runtime: 41 ms

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixMod = 0
        seen = {0:-1}
        for i in range(len(nums)):
            prefixMod = (prefixMod + nums[i])%k
            if prefixMod in seen :
                if i - seen[prefixMod] > 1:
                    return True
            else:
                seen[prefixMod] = i
        return False