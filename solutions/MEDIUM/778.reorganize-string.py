# Problem ID: 778
# Title: Reorganize String
# Runtime: 4 ms

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0]*26
        res = [None]* len(s)
        mxFreq = 0
        for char in s:
            freq[ord(char)-ord('a')]+=1
            mxFreq = max(mxFreq,freq[ord(char)-ord('a')])
        if mxFreq > (len(s)+1)//2:
            return ""
        
        l = sorted(list(set(s)), key = lambda x: freq[ord(x)-ord('a')], reverse = True)

        i = 0
        for char in l:
            for _ in range(freq[ord(char)-ord('a')]):
                if i>= len(s):
                    i = 1
                res[i] = char
                i+=2
        return "".join(res) 
