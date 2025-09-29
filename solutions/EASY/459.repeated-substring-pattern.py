# Problem ID: 459
# Title: Repeated Substring Pattern
# Runtime: 48 ms

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l=len(s)
        for i in range (len(s)//2):
            k=""
            if l%(i+1)==0:
                k=s[0:i+1]
                if k*(l//(i+1)) == s:
                    return True
        return False