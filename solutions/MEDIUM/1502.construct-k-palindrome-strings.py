# Problem ID: 1502
# Title: Construct K Palindrome Strings
# Runtime: 102 ms

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = 0
        freq = [0] * 26
        for char in s:
            i = ord(char) - ord('a')
            freq[i] += 1
            if freq[i]%2:
                cnt+=1
            else:
                cnt-=1
        return cnt<=k<=len(s)