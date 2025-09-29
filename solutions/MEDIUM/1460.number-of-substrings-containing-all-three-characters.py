# Problem ID: 1460
# Title: Number of Substrings Containing All Three Characters
# Runtime: 103 ms

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = [-1,-1,-1]
        def hasAllThree():
            for p in pos:
                if p == -1:
                    return False
            return True
        n = len(s)
        res = 0
        for i in range(n):
            ind = ord(s[i]) - ord("a")
            pos[ind] = i
            if hasAllThree():
                res += min(pos)+1
        return res
            

