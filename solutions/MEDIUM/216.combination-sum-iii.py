# Problem ID: 216
# Title: Combination Sum III
# Runtime: 0 ms

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backTrack(start,target, temp):
            if len(temp) == k:
                if target == 0:
                    ans.append(temp)
                return
            
            for i in range(start+1,10):
                if i <= target:
                    backTrack(i, target - i, temp+[i])
                else:
                    return
        
        backTrack(0, n, [])
        return ans