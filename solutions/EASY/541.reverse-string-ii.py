# Problem ID: 541
# Title: Reverse String II
# Runtime: 28 ms

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        l=len(s)
        ans=""
        while i<l:
            if l-i-1<k:
                ans+=s[i:l][::-1]
                break
            if l-i<2*k:
                ans+=s[i:i+k][::-1]
                ans+=s[i+k:l]
                break
            ans+=s[i:i+k][::-1]
            ans+=s[i+k:i+2*k]
            i+=2*k
        return ans