# Problem ID: 3430
# Title: Count Days Without Meetings
# Runtime: 150 ms

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda l:l[0])
        prevStart, prevEnd = meetings[0]
        cnt = prevStart-1
        for start, end in meetings[1:]:
            cnt += max(start - prevEnd - 1,0)
            prevEnd = max(prevEnd,end)
        cnt+= days - prevEnd
        return cnt