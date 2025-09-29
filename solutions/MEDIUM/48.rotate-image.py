# Problem ID: 48
# Title: Rotate Image
# Runtime: 0 ms

class Solution:
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if j<i:
                    matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

    def invertRows(self,matrix):
        for row in matrix:
            row.reverse()

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.invertRows(matrix)
        
