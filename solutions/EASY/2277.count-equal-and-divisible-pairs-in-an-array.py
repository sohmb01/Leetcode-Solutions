# Problem ID: 2277
# Title: Count Equal and Divisible Pairs in an Array
# Runtime: 15 ms

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j] and not (i*j)%k:
                    pairs+=1
        return pairs