# Problem ID: 1036
# Title: Rotting Oranges
# Runtime: 5 ms

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = collections.deque()
        cnt = 0
        rows, cols = len(grid),len(grid[0])
        visited = grid
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 2:
                    rotten.append((i,j))
                elif visited[i][j] == 1:
                    cnt +=1

        if cnt ==0:
            return 0 
        if not rotten:
            return -1
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        mins = -1
        while rotten:
            size = len(rotten)
            while size>0:
                x, y = rotten.popleft()
                for dx,dy in dirs:
                    i,j = x+dx,y+dy
                    if 0<=i<rows and 0<=j<cols and visited[i][j]==1:
                        cnt-=1
                        rotten.append((i,j))
                        visited[i][j] = 2
                size-=1
            mins+=1

        print(visited)
        if cnt != 0:
            return -1
        return mins