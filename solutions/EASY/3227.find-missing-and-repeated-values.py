# Problem ID: 3227
# Title: Find Missing and Repeated Values
# Runtime: 3 ms

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = (len(grid)**2) + 1
        freq = [0] * n
        for row in grid:
            for val in row:
                freq[val] +=1 
        ans = [-1,-1]
        for i in range(1,n):
            if not freq[i]:
                ans[1] = i 
            if freq[i] == 2:
                ans[0] = i
        return ans
            
