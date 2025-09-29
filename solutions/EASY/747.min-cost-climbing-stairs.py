# Problem ID: 747
# Title: Min Cost Climbing Stairs
# Runtime: 49 ms

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        
        a,b = 0, 0
        for i in range(len(cost)):
            a,b = b, min(a,b)+cost[i]
        return min(a,b)
        