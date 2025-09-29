# Problem ID: 801
# Title: Is Graph Bipartite?
# Runtime: 14 ms

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        a,b = set(),set()
        n = len(graph)
        visit = [False] * n

        def dfs(node, group):
            if visit[node]:
                if group:
                    a.add(node)
                else:
                    b.add(node)
                return
            visit[node] = True
            if group:
                a.add(node)
            else:
                b.add(node)

            for nei in graph[node]:
                dfs(nei, not group)
        dfs(0, True)
        for node in range(n):
            if not visit[node]:
                dfs(node, True)
        
        for ele in a:
            if ele in b:
                return False
            

        return True
                
