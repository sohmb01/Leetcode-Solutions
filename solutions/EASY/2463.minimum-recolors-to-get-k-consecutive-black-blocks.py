# Problem ID: 2463
# Title: Minimum Recolors to Get K Consecutive Black Blocks
# Runtime: 0 ms

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        dp = [0] * n
        whites = 0
        for i in range(k):
            if blocks[i] == "W":
                whites+=1
            dp[i] = whites
            
        ans = dp[k-1]
        for i in range(k,n):
            if blocks[i-k] == "W":
                whites-=1
            if blocks[i] == "W":
                whites+=1
            dp[i] = whites
            ans = min(dp[i],ans)
        return ans