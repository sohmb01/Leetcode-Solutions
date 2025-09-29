# Problem ID: 3627
# Title: Find Minimum Time to Reach Last Room I
# Runtime: 124 ms

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        dirs = ((0,-1),(0,1),(-1,0),(1,0))
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        heap = [(0,0,0)]
        while heap:
            currTime, i, j = heappop(heap)
            if i == rows-1 and j == cols-1:
                return currTime
            for di,dj in dirs:
                ni = i + di
                nj = j + dj
                if ni<0 or ni==rows or nj<0 or nj==cols:
                    continue
                newTime = max(moveTime[ni][nj], currTime)+1
                if newTime < dp[ni][nj]:
                    dp[ni][nj] = newTime
                    heappush(heap,(newTime,ni,nj))
        return 0