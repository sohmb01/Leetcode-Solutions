# Problem ID: 1063
# Title: Best Sightseeing Pair
# Runtime: 65 ms

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        l = values[0]
        for i in range(1,len(values)):
            ans = max(ans,values[i]-i+l)
            l = max(l,values[i]+i)
        return ans
