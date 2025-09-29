# Problem ID: 59
# Title: Spiral Matrix II
# Runtime: 0 ms

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat =  [[0 for _ in range(n)] for _ in range(n)]
        i,j,curr = 0,0,0
        dx,dy = 1,0
        while curr < n**2:
            curr+=1
            mat[i][j] = curr
            if i+dy==n or j+dx==n or mat[i+dy][j+dx]!=0:
                dx,dy = -dy,dx
            i+=dy
            j+=dx
        return mat
        