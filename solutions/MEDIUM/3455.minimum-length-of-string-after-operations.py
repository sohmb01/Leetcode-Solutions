# Problem ID: 3455
# Title: Minimum Length of String After Operations
# Runtime: 275 ms

class Solution:
    def minimumLength(self, s: str) -> int:
        
        ans = 0
        freq = [0]*26
        for char in s:
            index = ord(char) - ord('a')
            freq[index] += 1
        for cnt in freq:
            while cnt >= 3:
                cnt = cnt//3 + cnt%3
            ans+=cnt
        return ans

