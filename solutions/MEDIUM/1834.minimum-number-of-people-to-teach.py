# Problem ID: 1834
# Title: Minimum Number of People to Teach
# Runtime: 150 ms

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        need = set()
        for u,v in friendships:
            u-=1
            v-=1
            canTalk = False
            for x in languages[u]:
                if x in languages[v]:
                    canTalk = True
                    break
            if not canTalk:
                need.add(u)
                need.add(v)
        
        ans = len(languages) + 1
        for i in range(1,n+1):
            c = 0
            for v in need:
                if i not in languages[v]:
                    c+=1
            ans = min(ans, c)
        return ans

