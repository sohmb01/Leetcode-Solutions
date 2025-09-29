# Problem ID: 1851
# Title: Maximum Number of Events That Can Be Attended II
# Runtime: 669 ms

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [event[0] for event in events]
        
        dp = [[-1] * n for _ in range(k+1)] 
        
        def dfs(curr, cnt):
            if cnt == 0 or curr == n:
                return 0
            
            if dp[cnt][curr] != -1:
                return dp[cnt][curr]

            nextIdx = bisect_right(starts, events[curr][1])
            
            dp[cnt][curr] = max(dfs(curr+1,cnt),dfs(nextIdx,cnt-1)+events[curr][2])
            return dp[cnt][curr]
        
        return dfs(0,k)
