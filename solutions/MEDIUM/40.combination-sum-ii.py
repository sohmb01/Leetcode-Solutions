# Problem ID: 40
# Title: Combination Sum II
# Runtime: 3 ms

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        candidates.sort()
        def dfs(i, target):
            if target == 0:
                ans.append(temp[:])
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if candidates[j]>target:
                    break
                temp.append(candidates[j])
                dfs(j+1,target-candidates[j])
                temp.pop()
        dfs(0,target)
        return ans
