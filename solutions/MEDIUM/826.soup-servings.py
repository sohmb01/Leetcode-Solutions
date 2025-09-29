# Problem ID: 826
# Title: Soup Servings
# Runtime: 1787 ms

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 50000:
            return 1.0
        @cache
        def dfs(a,b):
            if a <= 0 and b>0:
                return 1
            if a<=0 and b<=0:
                return 0.5
            if a>=0 and b<=0:
                return 0
            else:
                return 0.25*(dfs(a-4,b)+dfs(a-3,b-1)+dfs(a-2,b-2)+dfs(a-1,b-3))
        
        N = (n+24)//25
        return dfs(N,N)
