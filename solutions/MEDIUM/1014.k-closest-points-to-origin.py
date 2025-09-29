# Problem ID: 1014
# Title: K Closest Points to Origin
# Runtime: 68 ms

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        ans = []
        for point in points:
            distance = (point[0]**2)+ (point[1]**2)
            heapq.heappush(ans,(-distance,point[0],point[1]))
            if len(ans)>k:
                heapq.heappop(ans)
        return [[x,y] for (dist,x,y) in ans]
            