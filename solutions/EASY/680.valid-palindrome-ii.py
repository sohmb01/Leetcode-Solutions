# Problem ID: 680
# Title: Valid Palindrome II
# Runtime: 56 ms

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isValidPalindrome(s):
            l,r = 0, len(s)-1
            while l<=r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        
        l,r = 0, len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return isValidPalindrome(s[l+1:r+1]) or isValidPalindrome(s[l:r])
            l+=1
            r-=1
        return True