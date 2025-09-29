# Problem ID: 3483
# Title: Alternating Groups II
# Runtime: 689 ms

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        colors += colors[:k-1]
        res = 0
        cnt = 1
        for i in range(1,len(colors)):
            if colors[i-1] != colors[i]:
                cnt+=1
            else:
                cnt = 1
            if cnt >= k:
                res+=1
        return res