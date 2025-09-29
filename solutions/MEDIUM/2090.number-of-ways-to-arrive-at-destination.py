# Problem ID: 2090
# Title: Number of Ways to Arrive at Destination
# Runtime: 18 ms

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))

        ways = [0] * n
        ways[0] = 1
        times = [float('inf')] * n
        pq = [(0,0)] #(cost,node)
        MOD = 10 ** 9 + 7
        while pq:
            time, node = heappop(pq)
            for nei, weight in adj[node]:
                if time+weight < times[nei]:
                    times[nei] = time+weight
                    ways[nei] = ways[node]
                    heappush(pq,(time+weight, nei))
                elif time+weight == times[nei]:
                    ways[nei] = (ways[nei] + ways[node] ) % MOD
        return ways[n-1]
                   

        
