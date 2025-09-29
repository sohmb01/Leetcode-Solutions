# Problem ID: 900
# Title: Reordered Power of 2
# Runtime: 3 ms

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def makeStr(x):
            return "".join(sorted([c for c in str(x)]))


        s = set()
        x = 1
        while x < min(n*10,10**9):
            s.add(makeStr(x))
            x *= 2
        
        return makeStr(n) in s
        