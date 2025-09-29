# Problem ID: 5
# Title: Longest Palindromic Substring
# Runtime: 199 ms

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==1:
            return s

        def expand(l,r):
            while (l>=0 and r<n and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        
        max_len = 0
        ans = ""
        for i in range(n-1):
            even = expand(i,i+1)
            odd = expand(i,i)
            if len(even) > len(odd) and len(even)>max_len:
                max_len = len(even)
                ans = even
            if len(even) < len(odd) and len(odd)>max_len:
                max_len = len(odd)
                ans = odd
        return ans
                  
            