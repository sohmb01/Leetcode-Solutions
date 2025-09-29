# Problem ID: 3754
# Title: Maximum Manhattan Distance After K Changes
# Runtime: 1434 ms

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        vertical,horizontal = 0,0
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if c == "N":
                vertical+=1
            elif c=="S":
                vertical-=1
            elif c=="E":
                horizontal+=1
            else:
                horizontal-=1
            
            ans = max(ans, min(abs(vertical)+abs(horizontal)+ k*2, i+1))
        return ans