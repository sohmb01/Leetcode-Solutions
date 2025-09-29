# Problem ID: 670
# Title: Maximum Swap
# Runtime: 0 ms

class Solution:
    def maximumSwap(self, num: int) -> int:
        li = [int(x) for x in str(num)]
        mxDigit, mxIdx, l,r = -1,-1,-1,-1
        for i in range(len(li)-1,-1,-1):
            if mxDigit < li[i]:
                mxDigit = li[i]
                mxIdx = i
            if mxDigit > li[i]:
                l = i
                r = mxIdx
        if l != -1:
            li[l],li[r] = li[r],li[l]
        return int("".join([str(x) for x in li]))


            