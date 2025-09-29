# Problem ID: 1843
# Title: Number Of Rectangles That Can Form The Largest Square
# Runtime: 180 ms

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l= [min(rectangles[i][0],rectangles[i][1]) for i in range (len(rectangles))]
        m=max(l)
        return l.count(m)