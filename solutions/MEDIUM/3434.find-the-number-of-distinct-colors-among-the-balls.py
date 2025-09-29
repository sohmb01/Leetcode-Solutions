# Problem ID: 3434
# Title: Find the Number of Distinct Colors Among the Balls
# Runtime: 100 ms

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        mp = {}
        colors = defaultdict(int)
        cnt = 0
        ans = []
        for ball, color in queries:
            if mp.get(ball,-1) == color:
                ans.append(cnt)
                continue
            x = mp.get(ball,-1)
            if mp.get(ball,-1) != -1:
                colors[x]-=1
            mp[ball] = color
            colors[color] += 1
            if x != -1 and not colors[x]:
                cnt -=1
            if colors[color] == 1 :
                cnt+=1
            ans.append(cnt)
        return ans


                
                

            



                
                
