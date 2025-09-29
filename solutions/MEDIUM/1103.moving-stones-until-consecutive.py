# Problem ID: 1103
# Title: Moving Stones Until Consecutive
# Runtime: 0 ms

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c = sorted([a,b,c])
        mnMoves = 0
        if b-a != 1:
            mnMoves+=1
        if c-b != 1:
            mnMoves+=1
        if b-a==2 or c-b==2:
            mnMoves = 1

        mxMoves = c-a-2
        return [mnMoves, mxMoves]
