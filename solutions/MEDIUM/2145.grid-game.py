# Problem ID: 2145
# Title: Grid Game
# Runtime: 79 ms

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = float('inf')
        s = sum(grid[0])
        bottomSum = 0
        for i in range(n):
            s -= grid[0][i]
            ans = min(ans,max(bottomSum,s))
            bottomSum+=grid[1][i]
            
        return ans
        
                    
