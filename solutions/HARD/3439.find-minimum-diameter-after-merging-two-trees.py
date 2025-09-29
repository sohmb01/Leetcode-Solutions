# Problem ID: 3439
# Title: Find Minimum Diameter After Merging Two Trees
# Runtime: 709 ms

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def dfs(node,parent,adj):
                mxDiameter = 0
                heap = [0,0]
                for neighbor in adj[node]:
                    if neighbor == parent:
                        continue
                    childDiameter, childPath = dfs(neighbor,node,adj)
                    mxDiameter = max(childDiameter, mxDiameter)
                    heappush(heap,childPath)
                    heappop(heap)
                mxDiameter = max(mxDiameter, sum(heap))
                return [mxDiameter, 1+ max(heap)]

        def findDiameter(edges):
            if len(edges) == 0:
                return 0
            adj = defaultdict(list)
            
            for i,j in edges:
                adj[i].append(j)
                adj[j].append(i)
            
            diameter, _ = dfs(0,-1,adj)
            return diameter

        d1 , d2 = findDiameter(edges1), findDiameter(edges2)
        return max(d1,d2, 1+ceil(d1/2)+ceil(d2/2))
        

                