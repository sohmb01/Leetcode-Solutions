# Problem ID: 1056
# Title: Capacity To Ship Packages Within D Days
# Runtime: 295 ms

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isValid(capacity):
            day = 1
            curr = 0
            for i in range(len(weights)):
                if curr + weights[i] <= capacity:
                    curr+=weights[i]
                else:
                    curr = weights[i]
                    day+=1
                if day > days:
                    return False
            return True

        l,r = max(weights), sum(weights)

        while l<=r:
            m = (l+r+1)//2
            if isValid(m):
                r = m-1
            else:
                l = m+1

        return l 