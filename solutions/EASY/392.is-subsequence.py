# Problem ID: 392
# Title: Is Subsequence
# Runtime: 32 ms

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        if len(s)==1 and s in t:
            return True
        if not s:
            return True
        for i in range(len(t)):
            if t[i]==s[0]:
                return self.isSubsequence(s[1:],t[i+1:])
        return False