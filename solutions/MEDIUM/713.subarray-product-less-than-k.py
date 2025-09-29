# Problem ID: 713
# Title: Subarray Product Less Than K
# Runtime: 46 ms

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        l,r = 0,0
        product = 1
        n = len(nums)
        res = 0
        for r in range(n):
            product*=nums[r]
            while product>=k:
                product//=nums[l]
                l+=1
            res += r-l+1
                
        return res

