# Problem ID: 118
# Title: Pascal's Triangle
# Runtime: 0 ms

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for row in range(2,numRows+1):
            prev = res[-1]
            temp = [1]*row
            for col in range(1,row-1):
                temp[col] = prev[col-1]+prev[col]
            res.append(temp)
        return res

