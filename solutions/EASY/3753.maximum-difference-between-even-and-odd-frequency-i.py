# Problem ID: 3753
# Title: Maximum Difference Between Even and Odd Frequency I
# Runtime: 0 ms

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0]*26
        for c in s:
            freq[ord(c)-ord('a')]+=1

        mxa1,mxa2, mna1,mna2 = 0,0, len(s),len(s)
        for i in range(26):
            if freq[i]%2:
                mna1 = min(freq[i],mna1)
                mxa1 = max(freq[i],mxa1)
            elif freq[i]%2==0 and freq[i]!=0:
                mna2 = min(freq[i],mna2)
                mxa2 = max(freq[i],mxa2)
        
        return mxa1-mna2