# Problem ID: 125
# Title: Valid Palindrome
# Runtime: 44 ms

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for k in s:
            if k.isalnum():
                st+=k.lower()
        
        return st==st[::-1]