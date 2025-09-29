# Problem ID: 1558
# Title: Course Schedule IV
# Runtime: 39 ms

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        mp = defaultdict(set)
        for a,b in prerequisites:
            adj[b].append(a)
        
        visited = [False] * numCourses
        def dfs(node):
            if node in mp:
                return mp[node]
            for nei in adj[node]:
                mp[node] = mp[node] | dfs(nei)
            mp[node].add(node)
            return mp[node]

        for i in range(numCourses):
            dfs(i)
        res = []
        for x,y in queries:
            res.append(x in mp[y])
        return res