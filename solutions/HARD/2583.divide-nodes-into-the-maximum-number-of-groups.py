# Problem ID: 2583
# Title: Divide Nodes Into the Maximum Number of Groups
# Runtime: 1781 ms

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def getConnectedComponents(src):
            q = deque([src])
            components = set([src])
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei in components:
                        continue
                    q.append(nei)
                    components.add(nei)
                    visit.add(nei)
            return components

        def getLongestPath(src):
            q = deque([(src,1)])
            dist = { src : 1}
            while q:
                node, length = q.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] == length:
                            return -1
                        continue
                    q.append((nei,length+1))
                    dist[nei] = length+1
            return max(dist.values())

        res = 0
        visit = set()
        for i in range(1,n+1):
            if i in visit:
                continue
            components = getConnectedComponents(i)
            groups = 0
            for node in components:
                length = getLongestPath(node)
                if length == -1:
                    return -1
                groups = max(groups, length)
            res += groups
        return res
