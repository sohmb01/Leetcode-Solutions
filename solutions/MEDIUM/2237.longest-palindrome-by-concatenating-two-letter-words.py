# Problem ID: 2237
# Title: Longest Palindrome by Concatenating Two Letter Words
# Runtime: 36 ms

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt, res = Counter(words), 0
        for w, c in cnt.items(): # Address non-palindromic pairs
            rev = w[::-1]
            if w < rev and rev in cnt:
                res += 4 * min(c, cnt[rev])

        flag = False
        for w, c in cnt.items(): 
            if w[0] == w[1]:     
                res += 4 * (c // 2)
                if c%2:
                    flag = True
        if flag:
            res+=2
        
        return res

