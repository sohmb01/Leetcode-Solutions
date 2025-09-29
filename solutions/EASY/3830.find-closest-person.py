# Problem ID: 3830
# Title: Find Closest Person
# Runtime: 0 ms

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x-z) < abs(y-z):
            return 1
        elif abs(x-z) > abs(y-z):
            return 2
        else:
            return 0
