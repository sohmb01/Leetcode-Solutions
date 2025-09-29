# Problem ID: 581
# Title: Shortest Unsorted Continuous Subarray
# Runtime: 13 ms

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        l,r = -1,-1
        for i in range(len(nums)):
            if nums[i]!=sortedNums[i]:
                if l == -1:
                    l = i
                else:
                    r = i
        return r-l+1 if r!=-1 else 0