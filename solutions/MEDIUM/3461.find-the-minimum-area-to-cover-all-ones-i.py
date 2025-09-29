# Problem ID: 3461
# Title: Find the Minimum Area to Cover All Ones I
# Runtime: 2997 ms

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        ax,ay,bx,by = float('inf'), float('inf'),float('-inf'), float('-inf')
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ax = min(ax, i)
                    ay = min(ay, j)
                    bx = max(bx, i)
                    by = max(by, j)
                    cnt+=1
        

        return (by-ay+1) * (bx-ax+1) if cnt else 0

