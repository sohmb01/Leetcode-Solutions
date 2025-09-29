# Problem ID: 539
# Title: Minimum Time Difference
# Runtime: 15 ms

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToMinutes(ts):
            h,m = map(int,ts.split(":"))
            return h*60 + m
        
        timePoints = [convertToMinutes(tp) for tp in timePoints]
        timePoints.sort()
        timePoints.append(timePoints[0])

        res = 24*60
        for i in range(1,len(timePoints)):
            if timePoints[i]>=timePoints[i-1]:
                diff = timePoints[i]-timePoints[i-1]
            else:
                diff = timePoints[i] + 24*60 - timePoints[i-1]
            res = min(res,diff)
        return res