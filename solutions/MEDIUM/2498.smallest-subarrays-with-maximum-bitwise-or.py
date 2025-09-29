# Problem ID: 2498
# Title: Smallest Subarrays With Maximum Bitwise OR
# Runtime: 1726 ms

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        bits = [0] * 30
        for i in range(n-1,-1,-1):
            for bit in range(30):
                if nums[i] & (1<<bit) > 0:
                    bits[bit] = i
                res[i] = max(res[i],bits[bit]-i+1)
        return res