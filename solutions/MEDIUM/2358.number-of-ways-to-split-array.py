# Problem ID: 2358
# Title: Number of Ways to Split Array
# Runtime: 50 ms

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        cnt = 0
        total = sum(nums)
        curr = 0
        for i in range(len(nums)-1):
            curr+= nums[i]
            if curr >= total-curr:
                cnt+=1
        return cnt