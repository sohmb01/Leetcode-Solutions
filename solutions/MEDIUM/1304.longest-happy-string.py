# Problem ID: 1304
# Title: Longest Happy String
# Runtime: 0 ms

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heappush(heap,(-a,'a'))
        if b:
            heappush(heap,(-b,'b'))
        if c:
            heappush(heap,(-c,'c'))
        s = []
        while heap:
            cnt1, char1 = heappop(heap)
            if len(s)>=2 and s[-1] == char1 and s[-2] == char1:
                if not heap:
                    break
                cnt2,char2 = heappop(heap)
                s.append(char2)
                cnt2+=1
                if cnt2<0:
                    heappush(heap,(cnt2,char2))
                heappush(heap,(cnt1,char1))
            else:
                s.append(char1)
                cnt1+=1
                if cnt1<0:
                    heappush(heap,(cnt1,char1))
        return ''.join(s)