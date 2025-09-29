# Problem ID: 3279
# Title: Alice and Bob Playing Flower Game
# Runtime: 0 ms

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n//2) * ((m+1)//2) + (m//2) * ((n+1)//2)