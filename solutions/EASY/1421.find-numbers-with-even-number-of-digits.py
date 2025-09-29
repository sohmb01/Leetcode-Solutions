# Problem ID: 1421
# Title: Find Numbers with Even Number of Digits
# Runtime: 0 ms

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                cnt += 1
        return cnt
