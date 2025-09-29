# Problem ID: 2308
# Title: Divide Array Into Equal Pairs
# Runtime: 0 ms

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = [0] * 501
        for num in nums:
            freq[num] += 1
        for f in freq:
            if f%2:
                return False
        return True