# Problem ID: 3628
# Title: Find Minimum Time to Reach Last Room II
# Runtime: 1752 ms

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        rows, cols = len(moveTime),len(moveTime[0])
        heap = [(0,0,0,1)] # time, r, c, moves
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        flag = True
        while heap:
            time , i, j, moves = heappop(heap)
            if i == rows-1 and j == cols-1:
                return time
            for di, dj in dirs:
                ni,nj = i+di,j+dj
                if ni<0 or ni==rows or nj<0 or nj==cols:
                    continue
                newTime = max(time, moveTime[ni][nj]) + moves
                newMoves = 1 if moves == 2 else 2
                if newTime < dp[ni][nj]:
                    dp[ni][nj] = newTime
                    heappush(heap, (newTime,ni,nj,newMoves))
        return 0