# Problem ID: 242
# Title: Valid Anagram
# Runtime: 46 ms

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0]*26
        for char in s:
            l[ord(char) - ord('a')]+=1
        for char in t:
            l[ord(char) - ord('a')]-=1
        for netCount in l:
            if netCount != 0:
                return False
        return True
