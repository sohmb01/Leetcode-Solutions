# Problem ID: 2564
# Title: Most Profitable Path in a Tree
# Runtime: 233 ms

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        adj = defaultdict(list)
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        # Bob simulation
        bobTimes = {} #node : time visited
        def dfs(node, par, time):
            if node == 0:
                bobTimes[node] = time
                return True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei,node,time+1):
                    bobTimes[node] = time
                    return True
            return False

        dfs(bob, -1, 0)

        # Alice simulation
        res = float('-inf')
        q = deque([(0,0,-1,amount[0])]) # (node, time, parent, total profit)
        while q:
            node, time, parent, totalProfit = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                neiProfit = amount[nei]
                if nei in bobTimes:
                    if time+1 > bobTimes[nei]:
                        neiProfit = 0
                    elif time+1 == bobTimes[nei]:
                        neiProfit = neiProfit//2
                q.append((nei, time+1, node, totalProfit + neiProfit))
                if len(adj[nei]) == 1:
                    res = max(totalProfit + neiProfit,res)
            
        return res