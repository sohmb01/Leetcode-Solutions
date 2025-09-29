# Problem ID: 2527
# Title: Count Subarrays With Fixed Bounds
# Runtime: 154 ms

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        mn,mx,bad = -1,-1,-1
        res = 0
        for i, num in enumerate(nums):
            if num == minK:
                mn = i
            if num == maxK:
                mx = i
            if num < minK or num > maxK:
                bad = i
            if mn != -1 and mx != -1:
                res += max(0, min(mn,mx) - bad)
        return res