# Problem ID: 830
# Title: Largest Triangle Area
# Runtime: 171 ms

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def getArea(points):
            a,b,c = getDistance(points[0],points[1]),getDistance(points[1],points[2]),getDistance(points[0],points[2])
            if not isTriangle(a,b,c):
                return 0
            # Heron's formula
            s = (a+b+c)/2.0 #semiperimeter
            area = (s*(s-a)*(s-b)*(s-c))**0.5
            return area

        # get distance between a and b
        def getDistance(a,b):
            return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5
        
        # check if the points are triangle
        def isTriangle(a,b,c):
            return a+b>c and b+c>a and a+c>b
        
        n = len(points)
        maxArea = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    maxArea = max(maxArea, getArea([points[i],points[j],points[k]]))
        return maxArea
