# Problem ID: 3348
# Title: Minimum Cost Walk in Weighted Graph
# Runtime: 202 ms

class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        unionFind = UnionFind(n)
        for u,v,w in edges:
            unionFind.union(u,v)
        cost = {}
        ans = []
        for u,v,w in edges:
            root = unionFind.find(u)
            if root not in cost:
                cost[root] = w
            else:
                cost[root] &= w
        
        for src,dest in query:
            r1,r2 = unionFind.find(src),unionFind.find(dest)
            if r1!= r2:
                ans.append(-1)
            else:
                ans.append(cost[r1])
        return ans