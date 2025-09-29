# Problem ID: 365
# Title: Water and Jug Problem
# Runtime: 0 ms

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x+y == target:
            return True
        if x+y < target:
            return False
        
        def gcd (x,y):
            if y ==0:
                return x
            else:
                return gcd(y,x%y)
        return target % gcd(x,y) == 0