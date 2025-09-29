# Problem ID: 475
# Title: Heaters
# Runtime: 34 ms

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        mxRad = 0
        for house in houses:

            pos = bisect_left(heaters,house)
            left = float('inf') if pos == 0 else house - heaters[pos-1]
            right = float('inf') if pos == len(heaters) else heaters[pos]-house
            closestHeater = min(left,right)
            mxRad = max(mxRad, closestHeater)
        return mxRad