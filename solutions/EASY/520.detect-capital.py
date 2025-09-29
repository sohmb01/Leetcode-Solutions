# Problem ID: 520
# Title: Detect Capital
# Runtime: 32 ms

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isCapital = lambda x : ord(x)<=ord('Z') and ord(x)>=ord('A')
        capitals = len([x for x in word if isCapital(x)])
        if capitals==0 or capitals==len(word) or (capitals==1 and isCapital(word[0])):
            return True
        return False