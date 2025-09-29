# Problem ID: 54
# Title: Spiral Matrix
# Runtime: 0 ms

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x,y = 0,0
        rows,cols = len(matrix),len(matrix[0])
        ans = []
        dx, dy =  0, 1   #1 0    0 -1   -1 0
        for _ in range(rows*cols):
            ans.append(matrix[x][y])
            matrix[x][y] = "#"
            nx , ny =  x + dx, y + dy
            if nx==rows or ny==cols or nx<0 or ny< 0 or matrix[nx][ny] == "#" :
                dx,dy = dy, -dx
            
            x,y = x + dx, y + dy
        return ans

                
