# Problem ID: 409
# Title: Longest Palindrome
# Runtime: 0 ms

class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        for ch in s:
            if ch in mp:
                mp[ch] +=1
            else:
                mp[ch] = 1
        oddFreqPresent = False
        length = 0
        for key, val in mp.items():
            if val % 2:
                oddFreqPresent = True
                length -= 1
            
            length += val
        if oddFreqPresent:
            length+=1
        return length

