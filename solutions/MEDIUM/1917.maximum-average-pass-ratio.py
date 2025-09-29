# Problem ID: 1917
# Title: Maximum Average Pass Ratio
# Runtime: 983 ms

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        s = 0
        heap = []
        for p,q in classes:
            s += p/q
            heap.append(((p-q)/(q*(q+1)), p, q))
        heapify(heap)

        for _ in range(extraStudents):
            r, p, q = heappop(heap)
            if r == 0:
                break
            s -= r
            r2 = (p-q)/ ((q+1.0) * (q+2.0))
            heappush(heap, (r2,p+1, q+1))
        return s/n
