# Problem ID: 120
# Title: Triangle
# Runtime: 3 ms

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        if rows ==1:
            return triangle[0][0]
        j = rows - 1
        while j>=1:
            upperRow = triangle[j-1]
            lowerRow = triangle[j]
            temp = []
            for i in range(j):
                temp.append(upperRow[i]+min(lowerRow[i],lowerRow[i+1]))
            triangle[j-1] = temp
            j-=1
        return temp[0]