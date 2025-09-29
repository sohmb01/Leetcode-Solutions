# Problem ID: 2438
# Title: Find Closest Node to Given Two Nodes
# Runtime: 309 ms

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        n = len(edges)
        
        dist1, dist2 = [-1] * n, [-1] * n

        def dfs(node, currDist, dist, visit):
            if visit[node] or node == -1:
                return 
            dist[node] = currDist
            visit[node] = True
            dfs(edges[node], currDist+1, dist, visit)
        
        dfs(node1, 0, dist1, [False] * n )
        dfs(node2, 0, dist2, [False] * n )

        ans = n
        idx = -1
        print(dist1)
        print(dist2)
        for i in range(n):
            if ans > max(dist1[i],dist2[i]) and min(dist1[i],dist2[i])!=-1:
                ans = max(dist1[i],dist2[i])
                idx = i
        print(ans)
        return idx