# Problem ID: 647
# Title: Palindromic Substrings
# Runtime: 97 ms

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(l,r):
            cnt = 0
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
                cnt+=1
            return cnt
        
        ans = 1
        for i in range(n-1):
            ans+=expand(i,i+1)
            ans+= expand(i,i)
        
        return ans