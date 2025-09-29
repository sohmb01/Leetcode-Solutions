# Problem ID: 1570
# Title: Final Prices With a Special Discount in a Shop
# Runtime: 2 ms

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [prices[-1]]
        l = len(prices)
        if l == 1:
            return l
        ans = [0] * l
        i = l-2
        while i>=0:
            while stack and stack[-1]>prices[i]:
                stack.pop()
            
            ans[i] = prices[i]
            if stack:
                ans[i] -= stack[-1]
            stack.append(prices[i])
            i-=1
        ans[-1] = prices[-1]
        return ans