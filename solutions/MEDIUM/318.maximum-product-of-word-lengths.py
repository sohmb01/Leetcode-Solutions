# Problem ID: 318
# Title: Maximum Product of Word Lengths
# Runtime: 191 ms

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        n = len(words)
        bitmasks = []
        for word in words:
            bitmask = 0
            for c in set(word):
                bitmask |= (1 << (ord(c)-ord('a'))) 
            bitmasks.append(bitmask)
        ans =0
        for i in range(n-1):
            for j in range(i+1,n):
                if not bitmasks[i] & bitmasks[j]:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans