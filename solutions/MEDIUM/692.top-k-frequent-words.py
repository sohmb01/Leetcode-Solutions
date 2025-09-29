# Problem ID: 692
# Title: Top K Frequent Words
# Runtime: 3 ms

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        for key, val in freq.items():
            heappush(heap, (-val, key))
        res = []
        i = 0
        while i < k:
            currFreq, curr = heappop(heap)
            res.append(curr)
            i+=1
            while i<k and currFreq == heap[-1][0]:
                currFreq, curr = heappop(heap)
                res.append(curr)
                i+=1
        return res