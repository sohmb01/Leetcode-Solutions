# Problem ID: 205
# Title: Isomorphic Strings
# Runtime: 32 ms

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd={}
        td={}
        for i in range(len(s)):
            sd[s[i]]=t[i]
            td[t[i]]=s[i]
        for i in range (len(s)):
            if sd[s[i]]!=t[i] or td[t[i]]!=s[i]:
                return False
        return True