# Problem ID: 2394
# Title: Count Subarrays With Score Less Than K
# Runtime: 109 ms

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        n = len(nums)
        l = 0
        for r in range(n):
            total += nums[r]
            while l <= r and total*(r-l+1) >= k:
                total -= nums[l]
                l+=1
            res += r-l+1
        return res