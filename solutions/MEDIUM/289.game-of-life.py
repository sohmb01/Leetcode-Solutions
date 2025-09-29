# Problem ID: 289
# Title: Game of Life
# Runtime: 0 ms

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board), len(board[0])
        ans = [[-1 for _ in range(cols)] for _ in range(rows)]

        def getLiveNeighbors(i,j):
            neighbors = 0
            neighbors = neighbors+1 if (i-1>=0 and j-1>=0 and board[i-1][j-1]) else neighbors
            neighbors = neighbors+1 if (i-1>=0 and board[i-1][j]) else neighbors
            neighbors = neighbors+1 if (i-1>=0 and j+1<cols and board[i-1][j+1]) else neighbors
            neighbors = neighbors+1 if (j+1<cols and board[i][j+1]) else neighbors
            neighbors = neighbors+1 if (i+1<rows and j+1<cols and board[i+1][j+1]) else neighbors
            neighbors = neighbors+1 if (i+1<rows and board[i+1][j]) else neighbors
            neighbors = neighbors+1 if (i+1<rows and j-1>=0 and board[i+1][j-1]) else neighbors
            neighbors = neighbors+1 if (j-1>=0 and board[i][j-1]) else neighbors
            return neighbors

        for i in range(rows):
            for j in range(cols):
                ans[i][j] = board[i][j]
                neighbors = getLiveNeighbors(i,j)
                if board[i][j]:
                    if neighbors<2 or neighbors>3:
                        ans[i][j] = 0
                else:
                    if neighbors == 3:
                        ans[i][j] = 1
        
        for i in range(rows):
            for j in range(cols):
                board[i][j] = ans[i][j]