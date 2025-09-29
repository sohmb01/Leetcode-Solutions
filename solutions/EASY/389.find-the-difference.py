# Problem ID: 389
# Title: Find the Difference
# Runtime: 1 ms

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cntS = Counter(s)
        cntT = Counter(t)
        for k,_ in cntT.items():
            if cntS[k]!=cntT[k]:
                return k
        