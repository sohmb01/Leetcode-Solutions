# Problem ID: 2204
# Title: Find Subsequence of Length K With the Largest Sum
# Runtime: 3 ms

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        nums = [(i,num) for i,num in enumerate(nums)]
        nums.sort(key = lambda x:x[1], reverse = True)
        nums = nums[:k]
        nums.sort(key = lambda x:x[0])
        nums = [num[1] for num in nums]
        return nums