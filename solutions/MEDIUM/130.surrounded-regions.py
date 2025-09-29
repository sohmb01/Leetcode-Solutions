# Problem ID: 130
# Title: Surrounded Regions
# Runtime: 11 ms

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l = []
        rows, cols = len(board),len(board[0])
        for i in range (rows):
            for j in range(cols):
                if (i==0 or j==0 or i==rows-1 or j==cols-1) and (board[i][j] == "O"):
                    l.append((i,j))
        
        ret = [["X" for _ in range(cols)] for _ in range(rows)] 
        
        visited = set()
        def dfs(i,j):
            if board[i][j] == "X":
                return
            ret[i][j] = "O"
            visited.add((i,j))
            for r,c in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                if 0<=r<rows and 0<=c<cols and (r,c) not in visited:
                    dfs(r,c)
        for r,c in l:
            dfs(r,c)
        for i in range (rows):
            for j in range(cols):
                board[i][j] = ret[i][j]
                    
