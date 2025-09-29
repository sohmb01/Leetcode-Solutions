# Problem ID: 58
# Title: Length of Last Word
# Runtime: 24 ms

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans=0
        i=len(s)-1
        while (i>=0 and s[i]==" "):
            i-=1
        while (i>=0):
            if s[i]==" ":
                break
            else:
                i-=1
                ans+=1
        return ans