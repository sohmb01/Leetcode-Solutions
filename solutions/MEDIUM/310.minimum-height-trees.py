# Problem ID: 310
# Title: Minimum Height Trees
# Runtime: 43 ms

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        leaves = deque([i for i in range(n) if degree[i]==1])
        remainingNodes = n
        while remainingNodes > 2:
            leavesCnt = len(leaves)
            remainingNodes -= leavesCnt
            for _ in range(leavesCnt):
                node = leaves.popleft()
                for nei in adj[node]:
                    degree[nei]-=1
                    if degree[nei] == 1:
                        leaves.append(nei)
        return list(leaves)
            

        