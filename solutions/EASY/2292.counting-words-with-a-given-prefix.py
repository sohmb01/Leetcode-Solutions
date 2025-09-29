# Problem ID: 2292
# Title: Counting Words With a Given Prefix
# Runtime: 0 ms

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        k = len(pref)
        ans = 0
        for word in words:
            if len(word)>=k and word[:k]==pref:
                ans+=1
        return ans