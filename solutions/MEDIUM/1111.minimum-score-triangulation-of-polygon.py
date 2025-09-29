# Problem ID: 1111
# Title: Minimum Score Triangulation of Polygon
# Runtime: 54 ms

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i,j):
            if j-i < 2:
                return 0
            if j-i == 2:
                return values[i]*values[i+1]*values[j]
            return min( values[i]*values[k]*values[j] + dp(i,k) + dp(k,j) for k in range(i+1,j))
        return dp(0,len(values)-1)
            