# Problem ID: 36
# Title: Valid Sudoku
# Runtime: 0 ms

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele != ".":
                    if (i,ele) in s or (ele,j) in s or (i//3,j//3,ele) in s:
                        return False
                    s.add((i,ele))
                    s.add((ele,j))
                    s.add((i//3,j//3,ele))
        return True