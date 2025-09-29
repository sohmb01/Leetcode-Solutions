# Problem ID: 435
# Title: Non-overlapping Intervals
# Runtime: 59 ms

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda x : x[1])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                ans+=1
            else:
                end = intervals[i][1]
        return ans