# Problem ID: 119
# Title: Pascal's Triangle II
# Runtime: 24 ms

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        i=1
        prev=[1]
        while i<=rowIndex+1:
            h=[]
            for k in range(i):
                if k==0 or k==i-1:
                    h.append(1)
                else:
                    h.append(prev[k-1]+prev[k])
            ans=h
            prev=h
            i+=1
        return ans