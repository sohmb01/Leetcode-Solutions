# Problem ID: 695
# Title: Max Area of Island
# Runtime: 31 ms

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ans = 0
        rows,cols = len(grid),len(grid[0])

        def bfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or (i,j) in visited or grid[i][j]==0:
                return 0
            visited.add((i,j))
            return 1 + bfs(i+1,j) + bfs(i-1,j) + bfs(i,j+1) + bfs(i,j-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    ans = max(ans,bfs(i,j))
        return ans
