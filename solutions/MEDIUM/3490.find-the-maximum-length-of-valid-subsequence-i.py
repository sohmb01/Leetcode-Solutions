# Problem ID: 3490
# Title: Find the Maximum Length of Valid Subsequence I
# Runtime: 325 ms

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = 0
        patterns = [[0,0], [0,1], [1,0],[1,1]]
        for pattern in patterns:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt%2]:
                    cnt+=1
                res = max(cnt, res)
        return res
