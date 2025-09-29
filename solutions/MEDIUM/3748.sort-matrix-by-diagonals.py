# Problem ID: 3748
# Title: Sort Matrix by Diagonals
# Runtime: 14 ms

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        for i in range(n):
            diag = []
            x,y = i,0
            for _ in range(n-i):
                diag.append(grid[x][y])
                x+=1
                y+=1
            diag.sort(reverse = True)
            x,y = i,0
            for _ in range(n-i):
                grid[x][y] = diag[y]
                x+=1
                y+=1

        print(grid)
        for i in range(1,n):
            diag = []
            x,y = 0, i
            for _ in range(n-i):
                diag.append(grid[x][y])
                x+=1
                y+=1
            diag.sort()
            x,y = 0,i
            for _ in range(n-i):
                grid[x][y] = diag[x]
                x+=1
                y+=1

        
        return grid
        