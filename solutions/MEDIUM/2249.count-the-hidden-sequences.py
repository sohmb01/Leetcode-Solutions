# Problem ID: 2249
# Title: Count the Hidden Sequences
# Runtime: 103 ms

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        x = y = curr = 0
        for d in differences:
            curr += d
            x = min(curr,x)
            y = max(curr,y)
            if y - x > upper - lower:
                return 0
        return upper - lower - y + x + 1