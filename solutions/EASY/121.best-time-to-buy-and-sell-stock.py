# Problem ID: 121
# Title: Best Time to Buy and Sell Stock
# Runtime: 64 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        mx=0
        l=len(prices)
        mn=prices[0]
        for i in prices:
            if i<mn:
                mn=i
            if mx<(i-mn):
                mx=i-mn
        return max(mx,0)