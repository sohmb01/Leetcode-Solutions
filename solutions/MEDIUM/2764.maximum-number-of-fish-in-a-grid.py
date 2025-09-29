# Problem ID: 2764
# Title: Maximum Number of Fish in a Grid
# Runtime: 267 ms

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(cell, visit, s):
            i,j = cell
            if cell in visit or not grid[i][j]:
                return 0
            visit.add(cell)
            s += grid[i][j]
            for di, dj in dirs:
                ni,nj = i+di, j+dj
                if 0<=ni < rows and 0<= nj < cols:
                    s = max(s, dfs((ni,nj),visit,s))
            return s
        ans = 0
        for i in range(rows):
            for j in range (cols):
                if grid[i][j]:
                    ans = max(ans,dfs((i,j),set(),0))
        return ans
            
            
            