# Problem ID: 2260
# Title: Divide a String Into Groups of Size k
# Runtime: 0 ms

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        n = len(s)
        s += fill*(k - n%k)
        res = []
        i = 0
        while i < n:
            res.append(s[i:i+k])
            i+=k
        return res
        