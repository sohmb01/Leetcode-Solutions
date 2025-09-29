# Problem ID: 3201
# Title: Distribute Candies Among Children II
# Runtime: 4985 ms

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        res = 0
        for k in range(min(n,limit)+1):
            target = n - k
            if target > 2 * limit:
                continue
            res += min(limit,target) - max(0,target-limit) + 1
        return res

