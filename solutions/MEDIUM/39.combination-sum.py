# Problem ID: 39
# Title: Combination Sum
# Runtime: 12 ms

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(curr, x , idx):
            if x > target:
                return
            if x == target:
                ans.append(curr)
                return 
            for i in range(idx,n):
                dfs(curr+[candidates[i]],x+candidates[i], i)
        dfs([], 0, 0)
        return ans