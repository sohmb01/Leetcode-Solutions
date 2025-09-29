# Problem ID: 207
# Title: Course Schedule
# Runtime: 3 ms

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = []
        indegree = [0]* numCourses
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while (len(queue)):
            node = queue.pop()
            for i in adj[node]:
                indegree[i]-=1
                if not indegree[i]:
                    queue.append(i)
        for i in indegree:
            if i:
                return False
        return True
            
