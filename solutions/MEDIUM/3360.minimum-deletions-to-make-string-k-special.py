# Problem ID: 3360
# Title: Minimum Deletions to Make String K-Special
# Runtime: 99 ms

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        freq = [0]*26
        for c in word:
            freq[ord(c)-ord("a")]+=1
        freq.sort()
        i = 0 
        while freq[i] == 0:
            i+=1
        freq = freq[i:]
        res = len(word)
        for base in freq:
            d = 0
            for f in freq:
                if f<base:
                    d+=f
                elif base+k < f:
                    d += f - (base+k)

            res = min(res,d)
        return res

            