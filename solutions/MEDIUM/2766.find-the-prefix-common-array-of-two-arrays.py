# Problem ID: 2766
# Title: Find the Prefix Common Array of Two Arrays
# Runtime: 7 ms

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a,b = set(),set()
        ans = []
        prevCnt = 0
        for i in range(len(A)):
            cnt = 0 
            a.add(A[i])
            if B[i] in a:
                cnt+=1
            b.add(B[i])
            if A[i] in b:
                cnt+=1
            prevCnt += cnt
            if A[i] == B[i]:
                prevCnt-=1
            ans.append(prevCnt)
        return ans