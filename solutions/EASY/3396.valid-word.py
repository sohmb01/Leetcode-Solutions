# Problem ID: 3396
# Title: Valid Word
# Runtime: 0 ms

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        
        hasVowel = False
        hasConsonant = False

        for c in word:
            if c.isalpha():
                if c.lower() in {"a","e","i","o","u"}:
                    hasVowel = True
                else:
                    hasConsonant = True
            elif not c.isdigit():
                return False
        return hasVowel and hasConsonant