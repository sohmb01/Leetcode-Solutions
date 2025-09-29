# Problem ID: 498
# Title: Diagonal Traverse
# Runtime: 0 ms

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        row, col, direction = 0, 0, 1  # 1 = up-right, -1 = down-left
        
        for _ in range(m * n):
            result.append(mat[row][col])
            
            if direction == 1:  # moving up-right
                if col == n - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:  # moving down-left
                if row == m - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1
        
        return result