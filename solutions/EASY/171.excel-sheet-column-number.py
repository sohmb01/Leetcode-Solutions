# Problem ID: 171
# Title: Excel Sheet Column Number
# Runtime: 36 ms

class Solution:
    def titleToNumber(self, s: str) -> int:
        n=len(s)
        ans=0
        p=0
        k=reversed(s)
        for i in k:
            ans+=((ord(i)-64) * (26**p))
            p+=1
        return ans