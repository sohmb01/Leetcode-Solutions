# Problem ID: 6
# Title: Zigzag Conversion
# Runtime: 15 ms

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows = [[] for _ in range(numRows)]
        idx, dy = 0, 1
        for ch in s:
            rows[idx].append(ch)
            if idx == 0:
                dy = 1
            if idx == numRows-1:
                dy = -1
            idx += dy
        ans = ""
        for row in rows:
            ans+= "".join(row)
        return ans