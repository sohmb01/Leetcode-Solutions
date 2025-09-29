# Problem ID: 2588
# Title: Maximum Number of Points From Grid Queries
# Runtime: 584 ms

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        sq = sorted([query,i] for i,query in enumerate(queries))
        rows, cols = len(grid), len(grid[0])
        pq = [(grid[0][0],0,0)] #(val,r,c)
        visit = set()
        points = 0
        ans = [0] * len(queries)
        visit.add((0,0))
        for query, index in sq:
            while pq and pq[0][0] < query:
                val,r,c = heappop(pq)
                points+=1
                for i,j in [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]:
                    if i<0 or i==rows or j<0 or j==cols or (i,j) in visit:
                        continue
                    heappush(pq,(grid[i][j],i,j))
                    visit.add((i,j))
            
            ans[index] = points
        return ans





