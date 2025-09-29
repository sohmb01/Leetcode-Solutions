# Problem ID: 1876
# Title: Map of Highest Peak
# Runtime: 725 ms

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        rows,cols = len(isWater), len(isWater[0])
        a = [[-1]*cols for _ in range(rows)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]:
                    q.append((i,j))
                    a[i][j] = 0

        while q:
            r,c = q.popleft()
            height = a[r][c]
            neighbors = [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            for i ,j in neighbors:
                if -1< i <rows and -1 < j< cols and  a[i][j] == -1:
                    a[i][j] = height+1
                    q.append((i,j))
        return a

        