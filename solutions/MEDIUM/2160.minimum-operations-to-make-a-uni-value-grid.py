# Problem ID: 2160
# Title: Minimum Operations to Make a Uni-Value Grid
# Runtime: 142 ms

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l = []
        for row in grid:
            l+=row
        l.sort()
        n = len(l)
        mean = int(sum(l)//n)
        diff = float('inf')
        target = l[n//2]
        moves = 0
        for num in l:
            if abs(num - target)%x == 0:
                moves+= abs(num - target)//x
            else:
                return -1
        return moves
                 
        