# Problem ID: 9
# Title: Palindrome Number
# Runtime: 40 ms

class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        r=len(s)-1
        l=0
        ans=True
        while(l<=r):
            if (s[l]==s[r]):
                l+=1
                r-=1
            else:
                ans=False
                break
        return ans