# Problem ID: 1519
# Title: Minimum Subsequence in Non-Increasing Order
# Runtime: 56 ms

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        target = sum(nums)//2
        res=[]
        nums.sort()
        while target>=0:
            p=nums.pop()
            target-=p
            res.append(p)
        return res
        