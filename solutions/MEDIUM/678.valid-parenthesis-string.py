# Problem ID: 678
# Title: Valid Parenthesis String
# Runtime: 0 ms

class Solution:
    def checkValidString(self, s: str) -> bool:
        lmin,lmax = 0,0
        i = 0
        while i<len(s):
            if s[i]=='(':
                lmin+=1
                lmax+=1
            elif s[i] == ')':
                lmin-=1
                lmax-=1
            else:
                lmin-=1
                lmax+=1
            if lmax<0:
                return False
            if lmin<0:
                lmin = 0
            i+=1
        return lmin == 0