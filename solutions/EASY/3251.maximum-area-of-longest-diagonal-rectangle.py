# Problem ID: 3251
# Title: Maximum Area of Longest Diagonal Rectangle
# Runtime: 0 ms

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mxDiag = 0
        area = 0
        for l,w in dimensions:
            diag = l**2 + w**2
            if diag > mxDiag:
                mxDiag = diag
                area = l*w
            elif diag == mxDiag:
                area = max(area, l*w)
        return area