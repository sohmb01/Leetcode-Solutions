# Problem ID: 200
# Title: Number of Islands
# Runtime: 241 ms

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j,grid):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="#" or grid[i][j]=="0":
                return
            grid[i][j] = "#"
            bfs(i,j+1,grid)
            bfs(i+1,j,grid)
            bfs(i-1,j,grid)
            bfs(i,j-1,grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    bfs(i,j,grid)
        return count