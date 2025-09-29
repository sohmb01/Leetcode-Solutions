# Problem ID: 368
# Title: Largest Divisible Subset
# Runtime: 217 ms

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        cache = {}
        def dfs(i):
            if i == n:
                return []
            if i in cache:
                return cache[i]
            res = [nums[i]]
            for j in range(i+1,n):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dfs(j)
                    if len(temp) > len(res):
                        res = temp
            cache[i] = res
            return res

        res = []
        for i in range(n):
            temp = dfs(i)
            if len(temp)>len(res):
                res = temp
        return res