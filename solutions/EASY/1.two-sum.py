# Problem ID: 1
# Title: Two Sum
# Runtime: 0 ms

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in hashMap.keys() and i != hashMap[target-nums[i]]:
                return [i,hashMap[target-nums[i]]]