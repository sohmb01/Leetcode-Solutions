# Problem ID: 2300
# Title: Construct String With Repeat Limit
# Runtime: 135 ms

class Solution:
    import heapq
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(c), freq) for c, freq in Counter(s).items()]
        heapq.heapify(heap)
        ans = ""
        while heap:
            c, freq = heapq.heappop(heap)
            while freq > repeatLimit and heap:
                ans += chr(-c) * repeatLimit
                freq -= repeatLimit
                a , b = heapq.heappop(heap)
                ans+= chr(-a) 
                if b>1:
                    heapq.heappush(heap,(a,b-1))

            ans+= chr(-c) * min(freq,repeatLimit)
        return ans