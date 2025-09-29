# Problem ID: 1706
# Title: Min Cost to Connect All Points
# Runtime: 1717 ms

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def manhattan(x,y):
            return abs(x[0]-y[0])+ abs(x[1]-y[1])

        n = len(points)
        adj = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1,n):
                d = manhattan(points[i],points[j])
                adj[i].append((d,j))
                adj[j].append((d,i))
        
        res, visited, heap, cnt = 0, [False]* n, adj[0], 1
        visited[0] = True
        heapify(heap)

        while heap:
            d, v = heappop(heap)
            if not visited[v]:
                visited[v] = True
                res += d
                cnt +=1
                for rec in adj[v]:
                    heappush(heap,rec)
            if cnt >= n:
                break
        return res

