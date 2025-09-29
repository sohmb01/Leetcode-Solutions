# Problem ID: 441
# Title: Arranging Coins
# Runtime: 36 ms

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return  int((((1+(8*n))**0.5)-1)//2)