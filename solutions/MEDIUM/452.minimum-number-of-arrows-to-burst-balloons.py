# Problem ID: 452
# Title: Minimum Number of Arrows to Burst Balloons
# Runtime: 198 ms

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        res = n
        last = points[0]
        for i in range(1,n):
            if last[1] >= points[i][0]:
                res-=1
                last = [max(last[0],points[i][0]),min(last[1],points[i][1])]
            else:
                last = points[i]
        return res
        