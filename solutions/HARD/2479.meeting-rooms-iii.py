# Problem ID: 2479
# Title: Meeting Rooms III
# Runtime: 160 ms

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        usedRooms, unusedRooms = [], list(range(n))
        heapify(unusedRooms)
        meetingCounts = [0]*n

        for start, end in sorted(meetings):
            while usedRooms and usedRooms[0][0] <= start:
                _,room = heappop(usedRooms)
                heappush(unusedRooms, room)
            if unusedRooms:
                room = heappop(unusedRooms)
                heappush(usedRooms,[end,room])
            else:
                availableTime, room = heappop(usedRooms)
                heappush(usedRooms, [availableTime + end - start, room ])
            meetingCounts[room]+=1
        return meetingCounts.index(max(meetingCounts))