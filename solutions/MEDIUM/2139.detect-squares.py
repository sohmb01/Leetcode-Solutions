# Problem ID: 2139
# Title: Detect Squares
# Runtime: 90 ms

class DetectSquares:
    from collections import defaultdict
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)]+=1

    def count(self, point: List[int]) -> int:
        squares = 0
        x1,y1 = point
        for (x2,y2), cnt in self.points.items():
            if abs(x1-x2) == abs(y1-y2) and x1-x2 != 0:
                corner1 = (x1,y2)
                corner2 = (x2,y1)
                if corner1 in self.points and corner2 in self.points:
                    squares += cnt * self.points[corner1] * self.points[corner2]
        return squares



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)