# Problem ID: 383
# Title: Ransom Note
# Runtime: 56 ms

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        k=list(magazine)
        for i in ransomNote:
            if i not in k:
                return False
            ind=k.index(i)
            k.pop(ind)
        return True