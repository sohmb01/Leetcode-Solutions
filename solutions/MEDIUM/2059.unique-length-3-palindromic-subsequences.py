# Problem ID: 2059
# Title: Unique Length-3 Palindromic Subsequences
# Runtime: 143 ms

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0
        l,r = [-1]*26, [-1]*26
        for ind in range(len(s)):
            i = ord(s[ind]) - ord('a')
            if l[i] == -1:
                l[i] = ind
            r[i] = ind
        print(l)
        print(r)
        for letter in letters:
            i = ord(letter) - ord('a')
            if l[i] != r[i]:
                st = set(s[l[i]+1:r[i]])
                print(st)
                ans+= len(st)
        return ans
