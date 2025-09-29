# Problem ID: 152
# Title: Maximum Product Subarray
# Runtime: 7 ms

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        l = len(nums)
        product = 1
        ans = -inf
        for i in range(l):
            product*= nums[i]
            ans = max(ans, product)
            if not product:
                product = 1
        
        product = 1
        for i in range(l-1, -1,-1):
            product*= nums[i]
            ans = max(ans, product)
            if not product:
                product = 1
        return ans
        