# Problem ID: 1104
# Title: Coloring A Border
# Runtime: 4 ms

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        rows, cols = len(grid), len(grid[0])
        border = []
        visit = [[False] * cols for _ in range(rows)]
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or visit[i][j] or grid[i][j] != grid[row][col]:
                return 
            visit[i][j] = True
            if i==0 or j==0 or i==rows-1 or j == cols-1 or len(set([grid[i-1][j],grid[i][j-1],grid[i+1][j],grid[i][j+1]]))>1:
                border.append([i,j])
            
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
        
        dfs(row,col)
        if not border:
            grid[row][col] = color
            return grid
        for i,j in border:
            grid[i][j] = color
        return grid