# Problem ID: 2387
# Title: Partition Array Such That Maximum Difference Is K
# Runtime: 107 ms

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        partitions = 0
        l,r = 0,0
        while r < n:
            while r<n and nums[r]-nums[l]<=k:
                r+=1
            partitions+=1
            l = r
        return partitions