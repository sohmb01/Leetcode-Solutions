# Problem ID: 451
# Title: Sort Characters By Frequency
# Runtime: 23 ms

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = (1,c)
            else:
                f,_ = freq[c]
                freq[c] = (f+1,c)
        l = list(freq.values())
        l.sort(key = lambda x:x[0], reverse = True)
        res = []
        for f, c in l:
            for _ in range(f):
                res.append(c)
        return "".join(res)