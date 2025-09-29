# Problem ID: 455
# Title: Assign Cookies
# Runtime: 164 ms

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt=0
        i,j=0,0
        
        while i< len(g):
            while i<len(g) and j< len(s):
                if g[i]<=s[j]:
                    cnt+=1
                    i+=1
                    j+=1
                else:
                    j+=1
            if j==len(s):
                break
        return cnt