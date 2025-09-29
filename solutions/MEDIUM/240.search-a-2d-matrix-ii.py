# Problem ID: 240
# Title: Search a 2D Matrix II
# Runtime: 157 ms

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix),len(matrix[0])
        i, j = 0, cols-1
        while j>=0 and i<rows:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i+=1
        return False
