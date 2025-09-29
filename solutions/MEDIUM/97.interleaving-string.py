# Problem ID: 97
# Title: Interleaving String
# Runtime: 38 ms

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i,j,k = 0,0,0
        l1,l2,l3 = len(s1),len(s2),len(s3)
        if l1 + l2 != l3:
            return False
        
        @cache
        def backtrack(i,j,k):
            if i==l1 and j==l2:
                return True
            if i<l1 and j<l2 and s1[i] == s3[k] and s2[j] == s3[k]:
                return backtrack(i+1,j,k+1) or backtrack(i,j+1,k+1)
            elif i<l1 and s1[i] == s3[k]:
                return backtrack(i+1,j,k+1)
            elif j<l2 and s2[j] == s3[k]:
                return backtrack(i,j+1,k+1)
            else:
                return False
        return backtrack(0,0,0)