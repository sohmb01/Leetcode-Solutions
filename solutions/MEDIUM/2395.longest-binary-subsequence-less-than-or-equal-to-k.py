# Problem ID: 2395
# Title: Longest Binary Subsequence Less Than or Equal to K
# Runtime: 0 ms

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        n = len(s)
        curr = 0
        zeroes = s.count("0")
        l = zeroes

        for i in range(n-1,-1,-1):
            if s[i]=="1":
                curr += (1 << (n-i-1))
                if curr <= k:
                    l += 1
                else:
                    break
        return l
                