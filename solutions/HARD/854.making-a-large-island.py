# Problem ID: 854
# Title: Making A Large Island
# Runtime: 1157 ms

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        groups = {}
        group = 2

        def bfs(i,j,group):
            if (i,j) in visit or i<0 or i==n or j<0 or j==n or grid[i][j]==0:
                return
            visit.add((i,j))
            grid[i][j] = group
            if group not in groups:
                groups[group] = 0
            groups[group] += 1
            dirs = [(i,j+1),(i,j-1),(i-1,j),(i+1,j)]
            for r,c in dirs:
                bfs(r,c,group)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i,j,group)
                    group+=1
        if group == 3:
            return min(n**2,groups[2]+1)

        def getNeighboringIslands(i,j,currGroups):
            if i<0 or i==n or j<0 or j==n or grid[i][j]==0 or grid[i][j] in currGroups:
                return 0
            currGroups.add(grid[i][j])
            return groups[grid[i][j]]

        ans = 0
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    currGroups = set()
                    temp = 1
                    dirs = [(i,j+1),(i,j-1),(i-1,j),(i+1,j)]
                    for r,c in dirs:
                        temp += getNeighboringIslands(r,c,currGroups)
                    ans = max(ans,temp)
        return ans