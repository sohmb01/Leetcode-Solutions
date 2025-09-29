# Problem ID: 3617
# Title: Find the Original Typed String I
# Runtime: 41 ms

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        last = 0
        res = 1
        i = 0
        while i < n:
            while i<n and word[i]==word[last]:
                i+=1
            res+= i-last-1
            last = i
        return res 