# Problem ID: 1264
# Title: Maximum Number of Words You Can Type
# Runtime: 0 ms

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        def isValid(word):
            for c in word:
                if c in brokenLetters:
                    return False
            return True
        return (len([word for word in text.split(" ") if isValid(word)]))