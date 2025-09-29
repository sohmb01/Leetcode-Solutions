# Problem ID: 820
# Title: Find Eventual Safe States
# Runtime: 40 ms

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node] = False
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            safe[node] = True
            return True

        
        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans

