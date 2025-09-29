# Problem ID: 396
# Title: Rotate Function
# Runtime: 163 ms

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        last, n = 0,len(nums)
        s = sum(nums)
        for i in range(n):
            last+= i*nums[i]
        res = last
        for i in range(1,n):
            temp = last + s -(n * nums[n-i])
            res = max(res, temp)
            last = temp
        return res