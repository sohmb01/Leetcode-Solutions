# Problem ID: 795
# Title: K-th Symbol in Grammar
# Runtime: 4 ms

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        elif k % 2:
            return self.kthGrammar(n-1, (k+1)/2)
        else:
            return (self.kthGrammar(n-1, (k)/2)+1)%2
