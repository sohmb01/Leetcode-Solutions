# Problem ID: 128
# Title: Longest Consecutive Sequence
# Runtime: 365 ms

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        length = 1
        for num in nums:
            if num-1 not in nums:
                length = 1
                while num+length in nums:
                    length+=1
            ans = max(length, ans)

        return ans