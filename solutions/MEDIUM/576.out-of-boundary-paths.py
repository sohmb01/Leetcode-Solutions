# Problem ID: 576
# Title: Out of Boundary Paths
# Runtime: 31 ms

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7

        @cache
        def bt(i,j,moves):
            if i == m or j==n or i<0 or j < 0:
                return 1
            if moves == 0:
                return 0
            return (bt(i-1,j,moves-1) + bt(i+1,j,moves-1) + bt(i,j-1,moves-1) + bt(i,j+1,moves-1))%mod
        return bt(startRow, startColumn, maxMove)
        
            

            




