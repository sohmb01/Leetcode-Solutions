# Problem ID: 399
# Title: Evaluate Division
# Runtime: 0 ms

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        nodes = set()
        for val, (u,v) in zip(values, equations):
            graph[u].append((v, val))
            graph[v].append((u, 1.0/val))
            nodes.add(u)
            nodes.add(v)
        

        def bfs(curr, target, product, par,visit):
            if curr in visit:
                return -1.0
            visit.add(curr)
            if curr == target:
                return product
            for nei, val in graph[curr]:
                if nei == par:
                    continue
                res = bfs(nei,target,product*val, curr, visit)
                if res != -1.0:
                    return res
            return -1.0
        
        res = []
        for u,v in queries:
            if u not in nodes or v not in nodes:
                res.append(-1.0)
            else:
                s = set()
                x = bfs(u, v, 1, -1,s)
                res.append(x)
        return res




