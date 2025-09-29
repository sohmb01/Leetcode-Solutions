# Problem ID: 547
# Title: Number of Provinces
# Runtime: 6 ms

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    adj[i].append(j)
        
        visit = [False]*n
        def dfs(node):
            if visit[node]:
                return False
            visit[node] = True
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)
            return True
        
        res = 0
        for i in range(n):
            if dfs(i):
                res+=1
        return res

        
