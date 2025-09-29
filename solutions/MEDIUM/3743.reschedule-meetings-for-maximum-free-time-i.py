# Problem ID: 3743
# Title: Reschedule Meetings for Maximum Free Time I
# Runtime: 35 ms

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        end = 0
        for i in range(len(startTime)):
            gap = startTime[i] - end
            gaps.append(gap)
            end = endTime[i]
        
        
        if eventTime - end:
            gaps.append(eventTime - end)

        
        windowLen = min(len(gaps),k + 1)

        if windowLen == len(gaps):
            return sum(gaps)
        
        s = sum(gaps[:windowLen])
        ans = s
        for r in range(windowLen,len(gaps)):
            l = r - windowLen
            s = s - gaps[l] + gaps[r]
            ans = max(ans,s)

            
        return ans
