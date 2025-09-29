# Problem ID: 3790
# Title: Fruits Into Baskets II
# Runtime: 19 ms

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        for fruit in fruits:
            isPlaced = False
            for i,capacity in enumerate(baskets):
                if fruit <= capacity:
                    baskets[i] = 0
                    isPlaced = True
                    break
            if isPlaced:
                n-=1
        return n

