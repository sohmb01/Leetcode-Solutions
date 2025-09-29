# Problem ID: 780
# Title: Max Chunks To Make Sorted
# Runtime: 0 ms

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        mx = -1
        for i in range(len(arr)):
            mx = max(mx,arr[i])
            if mx == i:
                chunks+=1
        return chunks