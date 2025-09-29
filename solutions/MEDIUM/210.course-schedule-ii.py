# Problem ID: 210
# Title: Course Schedule II
# Runtime: 239 ms

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)] 
        for l in prerequisites:
            adj[l[1]].append(l[0])
            indegree[l[0]]+=1
        
        ans = []
        for _ in range(numCourses):
            for i in range(numCourses):
                if indegree[i] == 0:
                    ans.append(i)
                    indegree[i]-=1
                    for j in adj[i]:
                        indegree[j]-=1
        return ans if len(ans) == numCourses else []


