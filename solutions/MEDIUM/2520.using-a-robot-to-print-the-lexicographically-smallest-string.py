# Problem ID: 2520
# Title: Using a Robot to Print the Lexicographically Smallest String
# Runtime: 316 ms

class Solution:
    def robotWithString(self, s: str) -> str:
    
        res = []
        t = []
        n = len(s)
        minChar = s[-1]
        suffix = list(s)
        for i in range(n-2,-1,-1):
            if s[i] < suffix[i+1]:
                suffix[i] = s[i]
            else:
                suffix[i] = suffix[i+1]

        i = 0
        while i < n:
            while t and t[-1] <= suffix[i]:
                res.append(t.pop())
            t.append(s[i])
            i+=1
        
        while t:
            res.append(t.pop())
        return "".join(res)

