# Problem ID: 3194
# Title: Find Words Containing Character
# Runtime: 4 ms

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        def hasCharacter(word):
            for c in word:
                if c == x:
                    return True
            return False

        res = []
        for i, word in enumerate (words):
            if hasCharacter(word):
                res.append(i)
        return res
        