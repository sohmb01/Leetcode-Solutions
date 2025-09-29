# Problem ID: 122
# Title: Best Time to Buy and Sell Stock II
# Runtime: 64 ms

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        if l<2:
            return 0
        ans=0
        i=0
        while i<l-1:
            k=i+1
            if prices[i]<prices[k]:
                while k<l-1 and prices[k]<prices[k+1]:
                    k+=1
                profit=prices[k]-prices[i]
                ans+=profit
                i=k+1
            else:
                i+=1
        return ans