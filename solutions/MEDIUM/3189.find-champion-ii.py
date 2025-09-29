# Problem ID: 3189
# Title: Find Champion II
# Runtime: 11 ms

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0]*n
        for edge in edges:
            indegree[edge[1]]+=1
        champion = -1
        for i in range(n):
            if indegree[i] == 0:
                if champion != -1:
                    return -1
                else:
                    champion = i
        return champion
            
