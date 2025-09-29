# Problem ID: 2685
# Title: First Completely Painted Row or Column
# Runtime: 57 ms

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat),len(mat[0])
        n = rows * cols
        rowInd, colInd = [-1]*(n+1), [-1]*(n+1)
        rcnt,ccnt = [0]*rows, [0]*cols
        for i in range(rows):
            for j in range(cols):
                ele = mat[i][j]
                rowInd[ele] = i
                colInd[ele] = j
        for i in range(n):
            r,c = rowInd[arr[i]],colInd[arr[i]]
            rcnt[r] +=1
            ccnt[c] +=1
            if rcnt[r] == cols or ccnt[c] == rows:
                return i