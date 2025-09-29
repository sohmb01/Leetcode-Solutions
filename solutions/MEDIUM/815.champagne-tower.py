# Problem ID: 815
# Title: Champagne Tower
# Runtime: 82 ms

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        dp = [[0]*102 for _ in range(101)]

        currRow = 1
        dp[1][1] = poured
        while currRow <= query_row:
            currGlass = 1
            while currGlass<=currRow:
                if dp[currRow][currGlass] > 1:
                    dp[currRow+1][currGlass] += (dp[currRow][currGlass]-1)/2.0
                    dp[currRow+1][currGlass+1] += (dp[currRow][currGlass]-1)/2.0
                currGlass+=1
            currRow+=1
        return min(1.0,dp[query_row+1][query_glass+1])