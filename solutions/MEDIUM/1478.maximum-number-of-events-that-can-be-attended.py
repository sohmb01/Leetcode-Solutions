# Problem ID: 1478
# Title: Maximum Number of Events That Can Be Attended
# Runtime: 143 ms

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        maxDay = max(event[1] for event in events)
        events.sort()
        pq = []
        ans, j = 0, 0
        for i in range(1,maxDay+1):
            while j<n and events[j][0] <= i:
                heappush(pq,events[j][1])
                j+=1
            while pq and pq[0]<i:
                heappop(pq)
            if pq:
                heappop(pq)
                ans += 1
        return ans