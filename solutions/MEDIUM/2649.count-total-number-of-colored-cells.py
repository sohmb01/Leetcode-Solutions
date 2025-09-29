# Problem ID: 2649
# Title: Count Total Number of Colored Cells
# Runtime: 0 ms

class Solution:
    def coloredCells(self, n: int) -> int:
        return n*(n-1)*4 // 2 +1


        