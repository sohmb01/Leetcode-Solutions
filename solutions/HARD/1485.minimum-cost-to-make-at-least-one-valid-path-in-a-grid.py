# Problem ID: 1485
# Title: Minimum Cost to Make at Least One Valid Path in a Grid
# Runtime: 223 ms

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        dirs = {
            1: (0,1),
            2: (0,-1),
            3: (1,0),
            4: (-1,0)
        }
        rows,cols = len(grid),len(grid[0])
        q = deque([(0,0,0)]) # (r,c,cost)
        min_cost = {}

        while q:
            print("%")
            r, c, cost = q.popleft()
            if r == rows-1 and c == cols-1:
                return cost

            for d in dirs:
                dr, dc = dirs[d]
                nr, nc = r+dr, c+dc
                newCost = cost if d == grid[r][c] else cost+1
                if (nr < 0 or nc < 0 or nr == rows or nc == cols or 
                    newCost >= min_cost.get((nr,nc),float('inf'))):
                    continue
                min_cost[(nr,nc)] = newCost
                if d == grid[r][c]:
                    print("#")
                    q.appendleft((nr,nc,newCost))
                else:
                    print("*")
                    q.append((nr,nc,newCost))