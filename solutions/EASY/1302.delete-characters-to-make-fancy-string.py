# Problem ID: 1302
# Title: Delete Characters to Make Fancy String
# Runtime: 511 ms

class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        i = 0
        res = ""
        while i<n:
            cnt = 1
            ch = s[i]
            while i < n-1 and s[i]==s[i+1]:
                cnt+=1
                i+=1
            res += ch*min(2,cnt)
            i+=1
        return res
            