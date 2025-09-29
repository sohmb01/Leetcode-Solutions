# Problem ID: 386
# Title: Lexicographical Numbers
# Runtime: 23 ms

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        size = 0
        
        def dfs(curr,limit):
            if curr > limit:
                return
            res.append(curr)
            for i in range(10):
                nxt = curr*10 + i
                if nxt > limit:
                    break
                else:
                    dfs(nxt,limit)
        
        for start in range(1,10):
            dfs(start,n)
        return res
            

            

