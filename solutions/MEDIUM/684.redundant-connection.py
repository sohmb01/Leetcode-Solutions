# Problem ID: 684
# Title: Redundant Connection
# Runtime: 3 ms

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1]*(n+1)
        def find(node):
            if node != par[node]:
                par[node] = find(par[node])
            return par[node]
            

        def union(u,v):
            p1,p2 = find(u),find(v)
            if p1 == p2:
                return True
            if rank[p1]>rank[p2]:
                par[p2] = p1
                rank[p2]+=rank[p1]
            else:
                par[p1] = p2
                rank[p1] += rank[p2]
            return False
        
        for u,v in edges:
            if union(u,v):
                return [u,v]
