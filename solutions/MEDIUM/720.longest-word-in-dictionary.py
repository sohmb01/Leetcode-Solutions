# Problem ID: 720
# Title: Longest Word in Dictionary
# Runtime: 8 ms

class Solution:
    def longestWord(self, words: List[str]) -> str:
        seen = set([""])
        words.sort()
        ans = ""
        for word in words:
            if word[:-1] in seen:
                seen.add(word)
                if len(ans)<len(word):
                    ans = word
        return ans