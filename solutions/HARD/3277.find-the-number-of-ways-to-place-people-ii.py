# Problem ID: 3277
# Title: Find the Number of Ways to Place People II
# Runtime: 1308 ms

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p: (p[0], -p[1]))

        n = len(points)
        cnt = 0

        for i in range(n):
            y1 = points[i][1]
            maxY = -float('inf')

            for j in range(i+1, n):
                y2 = points[j][1]
                if y2 <= y1:
                    if y2 > maxY:
                        cnt+=1
                        maxY = y2
        return cnt