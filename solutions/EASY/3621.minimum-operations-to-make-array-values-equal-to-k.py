# Problem ID: 3621
# Title: Minimum Operations to Make Array Values Equal to K
# Runtime: 81 ms

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort()
        if nums[0] < k :
            return -1
        i = len(nums)-1
        res = 0
        while i>=0 and nums[i] > k:
            res+=1
            i-=1
        return res