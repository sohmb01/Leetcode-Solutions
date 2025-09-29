# Problem ID: 2681
# Title: Put Marbles in Bags
# Runtime: 175 ms

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        n = len(weights)
        costs = []
        for i in range(1,n):
            costs.append(weights[i]+weights[i-1])
        costs.sort()
        print(costs)
        maxScore, minScore = 0,0
        for i in range(k-1):
            minScore += costs[i]
            maxScore += costs[n-i-2]
        return maxScore - minScore