# Problem ID: 1127
# Title: Last Stone Weight
# Runtime: 0 ms

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-weight for weight in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x!=y:
                heapq.heappush(stones,-abs(x-y))
        if stones:
            return -stones[0]
        return 0