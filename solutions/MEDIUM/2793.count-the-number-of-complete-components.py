# Problem ID: 2793
# Title: Count the Number of Complete Components
# Runtime: 35 ms

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node,l):
            visit[node] = True
            l.append(node)
            for nei in adj[node]:
                if not visit[nei]:
                    l = dfs(nei,l)
            return l


        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = [False]*n
        res = 0
        for v in range(n):
            if not visit[v]:
                component = dfs(v,[])
                flag = True
                componentLength = len(component)
                for node in component:
                    if len(adj[node]) != componentLength - 1 :
                        flag = False
                        break
                if flag:
                    res+=1
        return res
