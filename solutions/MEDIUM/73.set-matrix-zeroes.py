# Problem ID: 73
# Title: Set Matrix Zeroes
# Runtime: 1 ms

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        firstRowZero = False
        firstColZero = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if j == 0:
                        firstColZero = True
                    if i == 0:
                        firstRowZero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        print(firstRowZero)
        for i in range(1,rows):
            if matrix[i][0] == 0:
                for j in range(1,cols):
                    matrix[i][j] = 0
        for j in range(1,cols):
            if matrix[0][j] == 0:
                for i in range(1,rows):
                    matrix[i][j] = 0
        
        if firstColZero and matrix[0][0] == 0:
            for j in range(rows):
                matrix[j][0] = 0

        if firstRowZero and matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0 
        