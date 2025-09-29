# Problem ID: 803
# Title: Cheapest Flights Within K Stops
# Runtime: 87 ms

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float('inf')]*n
        prices[src]=0

        for i in range(k+1):
            tmp = prices.copy()
            for s,d,p in flights:
                if prices[s] == float('inf'):
                    continue
                if p+prices[s] < tmp[d]:
                    tmp[d] = p+prices[s]
            prices = tmp

        return prices[dst] if prices[dst]!= float('inf') else -1
