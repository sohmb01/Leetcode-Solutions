# Problem ID: 542
# Title: 01 Matrix
# Runtime: 533 ms

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols = len(mat),len(mat[0])
        q = deque()
        ret = [ [ 10001 for _ in range(cols)] for _ in range(rows)]
        visit = [ [False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if not mat[i][j]:
                    q.append((i,j,0))
        
        def isValid(i,j):
            return not (i<0 or j<0 or i>=rows or j>=cols or visit[i][j])

        while q:
            r,c, dist = q.popleft()
            ret[r][c] = min(dist,ret[r][c])
            visit[r][c] = True
            for d in [(r,c+1),(r+1,c),(r-1,c),(r,c-1)]:
                i,j = d
                if isValid(i,j):
                    q.append((i,j,dist+1))
        return ret
