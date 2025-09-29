# Problem ID: 2887
# Title: Sort Vowels in a String
# Runtime: 114 ms

class Solution:
    def sortVowels(self, s: str) -> str:
        l = [c for c in s]
        vowels = [c for c in s if c.lower() in ['a','e','i','o','u']]
        vowels.sort()
        x = 0
        for i, c in enumerate(l):
            if c.lower() in ['a','e','i','o','u']:
                l[i] = vowels[x]
                x+=1
        return "".join(l)