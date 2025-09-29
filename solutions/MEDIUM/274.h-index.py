# Problem ID: 274
# Title: H-Index
# Runtime: 0 ms

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        ans = 0
        for i in range(n):
            length = n - i
            citation = min(citations[i],length)
            ans = max(ans,citation)
        return ans

