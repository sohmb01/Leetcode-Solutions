# Problem ID: 472
# Title: Concatenated Words
# Runtime: 314 ms

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        dic = set(words)
        res = []
        for word in words:
            l = len(word)
            dp = [False] * (l+1)
            dp[0] = True

            for i in range(1,l+1):
                for j in range((i==l) and 1 or 0, i):
                    if not dp[i]:
                        dp[i] = dp[j] and word[j:i] in dic
            if dp[l]:
                res.append(word)
        return res