# Problem ID: 1418
# Title: Fair Distribution of Cookies
# Runtime: 7277 ms

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        temp = [0] * k
        self.res = float('inf')
        def dfs(i,temp):
            if i == n:
                self.res = min(self.res, max(temp))
                return
            if max(temp) > self.res:
                return 
            for j in range(k):
                temp[j]+=cookies[i]
                dfs(i+1,temp)
                temp[j]-=cookies[i]
                
        dfs(0,temp)
        return self.res
