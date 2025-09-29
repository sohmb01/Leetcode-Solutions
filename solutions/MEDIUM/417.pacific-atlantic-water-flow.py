# Problem ID: 417
# Title: Pacific Atlantic Water Flow
# Runtime: 31 ms

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        atlantic = set()
        pacific = set()
        atlantic_visited = set()
        pacific_visited = set()
        def dfs(visited, i,j, val):
            if i<0 or j<0 or i==rows or j ==cols:
                return
            if (i,j) in visited:
                return
            if heights[i][j] < val:
                return 
            visited.add((i,j))
            dfs(visited, i-1, j, heights[i][j])
            dfs(visited, i+1, j, heights[i][j])
            dfs(visited, i, j-1, heights[i][j])
            dfs(visited, i, j+1, heights[i][j])
            
        for i in range(cols):
            dfs(pacific,0,i,heights[0][i])
            dfs(atlantic,rows-1,i, heights[rows-1][i])
        for i in range(rows):
            dfs(pacific,i,0,heights[i][0])
            dfs(atlantic,i,cols-1, heights[i][cols-1])
        ans = [cell for cell in (atlantic & pacific)]
        return ans

#    [1,2,3],
#    [8,9,4], 
#    [7,6,5]