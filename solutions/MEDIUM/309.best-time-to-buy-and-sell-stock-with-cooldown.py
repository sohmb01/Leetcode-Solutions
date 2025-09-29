# Problem ID: 309
# Title: Best Time to Buy and Sell Stock with Cooldown
# Runtime: 7 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = [[-1] * 2 for _ in range(len(prices))]
        def rec(day, buy):
            if day >= len(prices):
                return 0
            if memo[day][buy] != -1:
                return memo[day][buy]
            
            if buy:
                profit = max(-prices[day] + rec(day+1, 0), rec(day+1, 1))
            else:
                profit = max(prices[day] + rec(day+2, 1), rec(day+1, 0))
            memo[day][buy] = profit
            return memo[day][buy]
        return rec(0,1)
                
