# Problem ID: 2884
# Title: Length of the Longest Valid Substring
# Runtime: 1493 ms

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        forbidden = set(forbidden)
        ans = prev = 0
        for i in range(n):
            curr = i + 1
            for j in range(10):
                if i - j < 0:
                    break
                if word[i - j : i + 1] in forbidden:
                    curr = j
                    break
            curr = min(curr, prev + 1)
            ans = max(ans, curr)
            prev = curr
        return ans