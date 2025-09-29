# Problem ID: 3633
# Title: Maximize the Number of Target Nodes After Connecting Trees I
# Runtime: 1483 ms

class Solution:
    def buildAdjacencyList(self, edges):
        n = len(edges)+1
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def dfs(self, adj, k, par, node):
        if k<0:
            return 0
        cnt = 1
        for child in adj[node]:
            if child != par:
                cnt+= self.dfs(adj,k-1,node,child)
        return cnt
        

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        adj1 = self.buildAdjacencyList(edges1)
        adj2 = self.buildAdjacencyList(edges2)
        max2 = 0
        for i in range(len(edges2)+1):
            max2 = max(max2, self.dfs(adj2, k-1, -1, i))
        res = []
        for i in range(len(edges1)+1):
            res.append(max2 + self.dfs(adj1, k, -1, i))
        return res