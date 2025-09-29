# Problem ID: 467
# Title: Unique Substrings in Wraparound String
# Runtime: 54 ms

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        mp = defaultdict(int)
        mxLen = 0
        for i in range(len(s)):
            if i>0 and (ord(s[i])-ord(s[i-1]))%26 == 1:
                mxLen += 1
            else:
                mxLen = 1
            mp[s[i]] = max(mp[s[i]],mxLen)
        return sum(mp.values())