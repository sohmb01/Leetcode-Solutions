# Problem ID: 77
# Title: Combinations
# Runtime: 159 ms

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        visited = [False] * (n+1)
        def backtrack(i, res):
            if len(res) == k:
                ans.append(res)
                return
            for j in range(i,n+1):
                if not visited[j]:
                    visited[j] = True
                    backtrack(j+1, res + [j])
                    visited[j] = False
        backtrack(1,[])
        return ans
        
            