# Problem ID: 2448
# Title: Count Number of Bad Pairs
# Runtime: 87 ms

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(int)
        good = 0
        for i in range(n):
            diff = i - nums[i]
            good+= mp[diff]
            mp[diff]+=1
        total = (n*(n-1))//2
        return total - good

